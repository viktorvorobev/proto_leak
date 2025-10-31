Simple repo to reproduce an issue with https://github.com/protocolbuffers/protobuf/issues/10088

Uses [uv](https://docs.astral.sh/uv/) to work.

To python messages from .proto files, run:

```bash
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --proto_path=. schema.proto
```
