from django import template
from .. import SUBSTITUTION_USER_REQUEST_REAL_USER_KEY

register = template.Library()


@register.assignment_tag(takes_context=True)
@register.simple_tag(takes_context=True)
def substitution_user_get_real_user(context):
    return getattr(context.request, SUBSTITUTION_USER_REQUEST_REAL_USER_KEY, context.request.user)
