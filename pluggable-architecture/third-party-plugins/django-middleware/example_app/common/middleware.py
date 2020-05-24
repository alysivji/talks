import uuid


class RequestUuidMiddleware:
    """Add uuid to each request"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_id = request.headers.get("X-Request-ID")
        if not request_id:
            request_id = str(uuid.uuid4())
        request.request_id = request_id
        response = self.get_response(request)
        return response
