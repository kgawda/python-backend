import logging

logger = logging.getLogger(__name__)

def my_middleware(get_response):

    def middleware(request):
        if request.method == "POST" and "csrfmiddlewaretoken" in request.POST:
            # docelowo to powinien być .info albo .debug zamiast .warning
            logger.warning("POST Request: %s", request.POST)
        response = get_response(request)
        return response

    return middleware
