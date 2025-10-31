Simple repo to reproduce an issue with https://github.com/protocolbuffers/protobuf/issues/10088

Uses [uv](https://docs.astral.sh/uv/) to work.

To python messages from .proto files, run:

```bash
uv run -m grpc_tools.protoc --python_out=. --grpc_python_out=. --proto_path=. schema.proto
```

To run the scripts, use:

```bash
uv run leak.py
uv run no_leak.py
```
