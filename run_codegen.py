from grpc_tools import protoc

protoc.main((
    '',
    '-I.',
    '--python_out=.',
    '--grpc_python_out=.',
    './geobufv3.proto',
))
