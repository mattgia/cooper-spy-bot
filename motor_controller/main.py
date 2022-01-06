from dotenv import load_dotenv
load_dotenv()

from jsonrpc import JSONRPCResponseManager, dispatcher

import motor_service

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher
from werkzeug.datastructures import Headers


DEFAULT_SPEED = 40

@Request.application
def application(request):

    headers = Headers()
    headers.add("Access-Control-Allow-Origin", "*")
    headers.add("Access-Control-Allow-Headers", "*")
    headers.add("Access-Control-Allow-Methods", "*")

    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["forward"] = lambda : motor_service.forward(DEFAULT_SPEED)
    dispatcher["backward"] = lambda : motor_service.backward(DEFAULT_SPEED)
    dispatcher["turn_left"] = lambda : motor_service.turn_left(DEFAULT_SPEED)
    dispatcher["turn_right"] = lambda : motor_service.turn_right(DEFAULT_SPEED)
    dispatcher["stop"] = motor_service.stop 

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response('OK', mimetype='application/text', headers=headers)


if __name__ == '__main__':
    run_simple('0.0.0.0', 4000, application)
