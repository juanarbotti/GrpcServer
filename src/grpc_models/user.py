from datetime import datetime
import bcrypt

# Protobuffers modules
import protobuffers.user_proto.user_pb2 as user_pb2
import protobuffers.user_proto.user_pb2_grpc as user_pb2_grpc

# DB Module
from ops.db import get_session

# Sqlalchemy
import sqlalchemy.exc

# Database tools and models
from ops.db import get_session
from db_models.user import User

# Validator and message construction class for Users
from ops.user_ops import UserOps

# gRPC own utilities
from ops.grpcExt import ValArgumentError

# gRPC lib
import grpc

class UserService(user_pb2_grpc.UserServicer):

    def __init__(self):
        pass

    def CreateUpdate(self, request, context):
        
        # check input message fields before proceed
        try:
            UserOps.validate(request, context)
        except ValArgumentError as e:
            context.set_code(e.status_code)
            context.set_details(str(e))
            return user_pb2_grpc.Id()
        
        # If message is valid...
        # prepares data

        # Required values
        name = request.name
        surname = request.surname
        username = request.username
        email = request.email

        # Optional Values
        dob = None
        if request.HasField('dob'):
            dob = datetime.strptime(request.dob, "%Y-%m-%d")
            dob = dob.date()

        gender = None
        if request.HasField('gender'):
            gender = request.gender

        hashed_password = None
        if request.HasField('password'):
            password = request.password.encode('utf-8')
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            hashed_password = hashed_password.decode("utf-8")

        # Prepare all and store in database
        with get_session() as session:
            
            # operation is CREATE
            if not request.HasField('id'):
                
                # create the User object with required values
                user = User(
                    name = name,
                    surname = surname,
                    username = username,
                    email = email,
                    password = hashed_password # password is available in this case because validator makes required when creating a new user
                )
                
                # Check if optionals are available and then adds to User's object
                if dob:
                    user.dob = dob
                if gender:
                    user.gender = gender
                
                try: 
                    session.add(user)
                    session.commit()
                except sqlalchemy.exc.SQLAlchemyError as e:
                    error_message = str(e.args[0])
                    mensaje = "Problem saving to database: "+error_message
                    context.set_code(grpc.StatusCode.ABORTED)
                    context.set_details(mensaje)
                    return user_pb2.Id()

            
            # operation is UPDATE
            else: 
                
                user = session.query(User).get(request.id)
                if not user:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("User does not exist.")
                    return user_pb2.Id()
                
                user.name = name
                user.surname = surname
                user.username = username
                user.email = email
                user.dob = dob # Be careful, if message does not contain the field, it puts to null
                user.gender = gender # sames as dob
                if hashed_password: # But if password is not set, then it doesn't change it.
                    user.password = hashed_password

                try:
                    session.commit()
                except sqlalchemy.exc.SQLAlchemyError as e:
                    error_message = str(e.args[0])
                    mensaje = "Problem saving to database: "+error_message
                    context.set_code(grpc.StatusCode.ABORTED)
                    context.set_details(mensaje)
                    return user_pb2.Id()

                                    
            return user_pb2.Id(id=user.id)

    def Get(self, request, context):
        
        with get_session() as session:
            user = session.query(User).get(request.id)
            if user:
                return UserOps.create_message(user)
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("User not found")
                return user_pb2.response_user()
    
    def Delete(self, request, context):
        
        with get_session() as session:
            user = session.query(User).get(request.id)
            if user:
                session.delete(user)
                session.commit()
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("User not found")
            return user_pb2.Empty()

    def Search(self, request, context):

        with get_session() as session:

            # search by username, it can return multiple users    
            users = session.query(User).filter(
                User.username.like(f"%{request.text}%")
            ).all()

            if users:
                return UserOps.create_message_list(users)
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No results.")
                return user_pb2.response_user()