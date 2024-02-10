import sys
import os
from dotenv import load_dotenv

# Needed to run the server
from concurrent import futures
import grpc

# Load environment variables
load_dotenv()

# Database creation
def create_db():

    # Imports database management module
    import ops.db as db

    # Imports db models to create them
    from db_models.user import User
    
    # Create the models
    try:
        db.Base.metadata.create_all(db.engine)
    except Exception as exc:
        error = "Critical failure trying to create database: {}".format(str(exc))
        print(error)
        sys.exit(1)

# The GRPC Server
def serve():

    # Imports compiled GRPC
    import protobuffers.user_proto.user_pb2_grpc as pb2_grpc
    
    # Imports the GRPC model
    from grpc_models.user import UserService

    # Read ammount of workers for the server
    max_workers = os.getenv("MAX_WORKERS", 10)

    # Create server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=int(max_workers)))

    # Add servicers to server
    pb2_grpc.add_UserServicer_to_server(
        UserService(), server
    )

    # Reads server port
    server_port = os.getenv("GRPC_PORT",50051)

    # Finishes configuration and starts server
    server.add_insecure_port(f"[::]:{server_port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":

    # Create Database and Tables
    create_db()

    # Starts the server
    print("Starting GrpcServer")
    try:
        serve()
    except KeyboardInterrupt:
        print("\Server stopped.")

    sys.exit(0)