import uuid

from werkzeug.wrappers import Request


class RequestUuidMiddleware:
    """Add uuid to each request"""

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        request_id = request.headers.get("X-Request-ID")
        if not request_id:
            request_id = str(uuid.uuid4())
        environ["request_id"] = request_id
        return self.app(environ, start_response)
