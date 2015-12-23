from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import DetailView, View
from django.contrib.auth import get_user_model
from . import SUBSTITUTION_USER_SESSION_KEY, SUBSTITUTION_USER_REDIRECT_PATH, SUBSTITUTION_USER_REQUEST_REAL_USER_KEY


class SubstitutionUserTurnOnView(DetailView):
    model = get_user_model()

    def get(self, request, *args, **kwargs):
        if not getattr(request, SUBSTITUTION_USER_REQUEST_REAL_USER_KEY, request.user).is_superuser:
            return HttpResponseForbidden()
        super(SubstitutionUserTurnOnView, self).get(request, *args, **kwargs)
        request.session[SUBSTITUTION_USER_SESSION_KEY] = self.object.id
        return HttpResponseRedirect(SUBSTITUTION_USER_REDIRECT_PATH)

class SubstitutionUserTurnOffView(View):
    def get(self, request, *args, **kwargs):
        if not getattr(request, SUBSTITUTION_USER_REQUEST_REAL_USER_KEY, request.user).is_superuser:
            return HttpResponseForbidden()
        request.session[SUBSTITUTION_USER_SESSION_KEY] = None
        return HttpResponseRedirect(SUBSTITUTION_USER_REDIRECT_PATH)
