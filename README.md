## Contents

###  `/motor_controller`

This is a python app that controls the motor. There is a simple RPC server running that takes commands to control the motors.

#### How to run?
1. `pip3 install -r requirements.txt`
2. `python3 motor_controller/main.py
3. `python3 camera_stream/stream.py`


#### Sample curl for client
```
curl --location --request POST '192.168.2.2:4000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "method": "forward",
    "params": [],
    "jsonrpc": "2.0",
    "id": 0
}'
```