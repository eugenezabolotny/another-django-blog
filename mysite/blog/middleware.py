from django.http import HttpResponseRedirect


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if not request.user.is_authenticated:
            if not request.path.startswith('/login') and not request.path.startswith('/logout'):
                return HttpResponseRedirect('login')

        # Code to be executed for each request/response after
        # the view is called.

        return response
