from django.conf.urls import url
from .views import SubstitutionUserTurnOnView, SubstitutionUserTurnOffView

urlpatterns = [
    url(r'^substitution_user_turn_on/(?P<pk>\d+)/$', SubstitutionUserTurnOnView.as_view(),
        name='substitution_user_turn_on'),
    url(r'^substitution_user_turn_off/$', SubstitutionUserTurnOffView.as_view(), name='substitution_user_turn_off'),
]
