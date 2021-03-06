from django.middleware.common import CommonMiddleware


class CommonMiddlewareAppendSlashWithoutRedirect(CommonMiddleware):
    def process_request(self, request):
        if not request.path.endswith('/'):
            request.path = request.path + '/'
            request.path_info = request.path_info + '/'

        return None
