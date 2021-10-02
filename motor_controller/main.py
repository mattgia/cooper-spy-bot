from dotenv import load_dotenv
load_dotenv()

from jsonrpc import JSONRPCResponseManager, dispatcher

import motor_service

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher
from werkzeug.datastructures import Headers

@Request.application
def application(request):

    if request.method == "OPTIONS":
        headers = Headers()
        headers.add("Access-Control-Allow-Origin", "*")
        headers.add("Access-Control-Allow-Headers", "*")
        headers.add("Access-Control-Allow-Methods", "*")
        return Response(headers=headers)
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["forward"] = motor_service.forward
    dispatcher["backward"] = motor_service.backward
    dispatcher["turn_left"] = motor_service.turn_left
    dispatcher["turn_right"] = motor_service.turn_right
    dispatcher["stop"] = motor_service.stop 

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response('OK', mimetype='application/text')


if __name__ == '__main__':
    run_simple('0.0.0.0', 4000, application)
