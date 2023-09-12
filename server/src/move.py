from server.src.command import Command


class Move(Command):

    def __init__(self):
        super().__init__('move')

    def execute(self, request):
        if self.valid_request(request):
            pass
        else:
            return self.invalid_request_error()

    def valid_request(self, request):
        """Checks that the received request is valid"""

        if "robot" not in request or request["robot"] is None:
            return False
        elif "command" not in request or request["command"] is None:
            return False
        elif "arguments" not in request or request["arguments"] is None:
            return False
        elif type(request["arguments"]) is not list or len(request["arguments"]) != 0:
            return False
        else:
            return True

    def invalid_request_error(self):
        """Returns an error response when the request is invalid"""

        return {
            "result": "ERROR",
            "data": {
                "message": "Your request is not configured properly"
            }
        }
