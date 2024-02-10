# GrpcServer
## Example of GRPC API Server Implementation

This is an example of a gRPC API server that I created after extensive learning about gRPC. I strongly recommend managing datetime, time, and date types as strings in gRPC messages.

gRPC stands for "Google Remote Procedure Call." It is intended to be a way to communicate between machines. It's a good choice for communicating microservices because of its speed.

For more information about gRPC, visit https://grpc.io/.

## Python and gRPC
You can use grpcio and grpcio_tools package to create a server and interact with other gRPC servers. It has some 'tricky' things you will learn while using it. For example, if your message has 'optional' fields, you must check if field is set before trying to access the object. For example, you have a message with an optional field called 'gender' and it was not set in the message server receives.

```
    gender = request.gender
    print(gender)
```

will rise an error, because 'gender' is not in message. Instead you should do:
```
    gender = None
    if request.HasField('gender'):
        gender = request.gender
    print(gender)

    -> 'female'
```

## About This Code
This code is a simple example of how to manage user accounts. It currently has only one service, but you can create more. It uses an SQLite3 database for this purpose.

It supports all CRUD operations.

To try the server, I recommend using BloomRPC. Despite no longer being actively developed, it's a good choice because of its simplicity (https://github.com/bloomrpc/bloomrpc).

### File Structure

- **`README.md`:** Main documentation / this file.
- **`requirements.txt`:** Dependency list.
- **`docs/`:** Additional documentation.
- **`src/data`:** Path to the file database (SQLite3).
- **`src/db_models/user.py`:** SQLAlchemy User's model.
- **`src/grpc_models/user.py`:** The logic of the gRPC service for Users.
- **`src/ops/db.py`:** The module that handles database connections.
- **`src/ops/grpcExt.py`:** gRPC auxilary assets.
- **`src/ops/user_ops.py`:** Validation and message construction operation for User objects.
- **`protobuffers/user_proto`:** This folder contains the 'user.proto' model, and it will contain 'user_pb2_grpc.py' and 'user_pb2.py' after running 'gen_proto.py'.
- **`src/gen_proto.py`:** If you moidfy 'user.proto' file, you should run this in order to create/recreate the modules that will handle protocol buffer communications.
- **`src/run.py`:** Run the server.

## Installing and Running
1) Download and create a python 3 venv:
```
    cd GrpcServer
    python3 -m venv venv
    source venv/bin/activate
```
2) Install dependencies:
```
    pip install -r requierments.txt
```
3) Run the server
```
    python src/run.py
```

The defult port is 50051. You should connect to: http://localhost/50051 with your favourite gRPC client (I use BloomGRPC as I wrote above). If you're more begginer than I, please, do not try to access the url using a browser (it will not work) :).

## Docker Image
Clone the repository and run:
```
    docker-compose up -d --build
```
Port is setted to 50090 (see yaml file). You can map '/app/data' to a volume for database persistance.