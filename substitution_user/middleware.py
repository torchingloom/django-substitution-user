from django.contrib.auth import BACKEND_SESSION_KEY, load_backend
from . import SUBSTITUTION_USER_SESSION_KEY, SUBSTITUTION_USER_REQUEST_REAL_USER_KEY, \
    SUBSTITUTION_USER_REQUEST_PATH_EXCLUDES


class SubstitutionUserMiddleware(object):
    def process_request(self, request):
        if self.this_path_exclude_exclude(request.path):
            return
        if request.user.is_superuser and request.session.get(SUBSTITUTION_USER_SESSION_KEY, None):
            backend_path = request.session[BACKEND_SESSION_KEY]
            backend = load_backend(backend_path)
            setattr(request, SUBSTITUTION_USER_REQUEST_REAL_USER_KEY, request.user)
            request.user = backend.get_user(request.session[SUBSTITUTION_USER_SESSION_KEY])

    @classmethod
    def this_path_exclude_exclude(cls, path):
        for t in SUBSTITUTION_USER_REQUEST_PATH_EXCLUDES:
            if path.find(t) == 0:
                return True
        return False
