import os
from grpc_tools import protoc

##############################################
# This module compiles the GRPC .proto file. 
# You should run this if you modify user.proto file in src/protobuffers/user_proto directory.
# It will create new GRPC modules for managing Users.
#############################################

path = 'protobuffers/user_proto'
proto_file = os.path.join(path, 'user.proto')

protoc_args = [
    '-I',
    '--python_out=./',
    '--grpc_python_out=./',
    proto_file
]
try:
    protoc.main(protoc_args)
except Exception as e:
    print(f"Error compiling User protobuffer: {e}")
