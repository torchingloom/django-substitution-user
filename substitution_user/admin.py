from django.core.urlresolvers import reverse_lazy
from . import SUBSTITUTION_USER_ADMIN_COLUMN_NAME


class SubstitutionUserAdminMixin(object):
    def get_list_display(self, request):
        ret = list(super(SubstitutionUserAdminMixin, self).get_list_display(request))
        if request.user.is_superuser and '_substitution_user' not in ret:
            ret.append('_substitution_user')
        return ret

    def _substitution_user(self, obj):
        return '<a href="%s" target="_blank">%s</a>' % (
            reverse_lazy('substitution_user_turn_on', args=[obj.id]), SUBSTITUTION_USER_ADMIN_COLUMN_NAME)

    _substitution_user.short_description = SUBSTITUTION_USER_ADMIN_COLUMN_NAME
    _substitution_user.allow_tags = True
