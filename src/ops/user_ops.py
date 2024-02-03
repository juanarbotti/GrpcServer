from datetime import datetime
import re

from ops.grpcExt import ValArgumentError

# Database tools and models
from sqlalchemy import and_, or_
from ops.db import get_session
from db_models.user import User

import grpc
import protobuffers.user_proto.user_pb2 as user_pb2

class UserOps:

    @staticmethod
    def validate(request, context):

        # Username and email must be unique, but the rule is not defined in database declaration, 
        # so we will check that querying the database before proceeding.
        # This is the purpose of using a microservice for handling database logic (it can be changed 
        # without altering client`s logic).
        with get_session() as session:

            # For update operation:
            if request.HasField('id'):
                user_exists = session.query(User).filter(
                    and_(
                        or_(
                            User.username == request.username,
                            User.email == request.email
                        ),
                        User.id != request.id
                    )
                ).first()
            else: # for create operation
                user_exists = session.query(User).filter(
                    or_(
                        User.username == request.username,
                        User.email == request.email
                    ),
                ).first()

            if user_exists:
                raise ValArgumentError("A user has the same username and/or email address.", grpc.StatusCode.ALREADY_EXISTS)
            

        len_surname = len(request.surname)
        if len_surname < 1 or len_surname > 120:
            raise ValArgumentError("'surname' must be 1 to 120 characters long.")
        
        len_name = len(request.name)
        if len_name < 1 or len_name > 120:
            raise ValArgumentError("'name' must be 1 to 120 characters long.")
        
        # If message field is 'optional', you first have to check its presence befor accesing to it.
        if request.HasField('dob'):
            try:
                dob = datetime.strptime(request.dob,"%Y-%m-%d")
            except Exception as e:
                raise ValArgumentError("'dob' must respect this format: 'YYYY-mm-dd'")
            
        if request.HasField('gender'):
            len_gender = len(request.gender)
            if len_gender < 1 or len_gender > 32:
                raise ValArgumentError("'gender' must be 1 to 32 characteres long.")

        len_username = len(request.username)
        if len_username < 3 or len_username > 20:
            raise ValArgumentError("'username' must be 3 to 20 characters long.")
        
        len_email = len(request.email)
        if len_email > 320:
            raise ValArgumentError("'email' must be less than 320 characters long.")
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, request.email):
            raise ValArgumentError("'email' does not look like a valid email address.")

        if not request.HasField('password') and not request.HasField('id'):
            raise ValArgumentError("You must specify a password when creating a new user.")

        password = request.password
        if not password.isalnum():
            raise ValArgumentError("'password', must be alphanumeric.")

        # Remember: hashed password always has 60 characters long, but our condition is to be between 8 and 12.
        len_password = len(request.password)       
        if len_password < 8 or len_password > 32:
            raise ValArgumentError("'password' must be 8 to 32 characteres long.")

    @staticmethod
    def create_message(user):
        return user_pb2.response_user(
            id = user.id,
            surname = user.surname,
            name = user.name,
            dob = str(user.dob), # converts DATE object to string, otherwise will go into error
            gender = user.gender,
            username = user.username,
            email = user.email
        )
    
    @staticmethod
    def create_message_list(users):
        
        list_users = []
        for user in users:
            list_users.append(UserOps.create_message(user))

        return user_pb2.response_user_list(
            users = list_users
        )