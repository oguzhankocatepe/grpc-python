# grpc-python
gRPC implementation with Python
dart pub global activate protoc_plugin
export PATH="$PATH:$HOME/.pub-cache/bin"
sudo apt install python3-pip
pip install -r requirements.txt
python -m grpc_tools.protoc -Iprotos --python_out=. --pyi_out=. --grpc_python_out=. protos/plane.proto
source venv/bin/activate
pip install grpcio
pip install grpcio-tools
source /home/han/grpc/venv/bin/activate
sudo apt install python3.10-venv
python3 -m venv venv
sudo apt install build-essential gdb
