# Django substitution user

**django-substitution-user** is a project that makes it possible to substitute user, if you logged in as superuser 

## Installation
    pip install django-substitution-user

## Configuration
```python
# settings.py
INSTALLED_APPS = (
    # ...
    'substitution_user',
)
MIDDLEWARE_CLASSES = (
    # ...
    'substitution_user.middleware.SubstitutionUserMiddleware',
)

# urls.py
urlpatterns = patterns('',
    # ...
    url(r'^substitution_user/', include('substitution_user.urls')),
)
```

## Usage
### Admin
```python
# someapp/admin.py
# ...
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from substitution_user.admin import SubstitutionUserAdminMixin
# ...
@admin.register(get_user_model())
class UserAdmin(SubstitutionUserAdminMixin, UserAdminBase):
    pass
```

### Template
```html
{% load substitution_user %}
{% substitution_user_get_real_user as real_user %}
{% if real_user != request.user %}
    <a href="{% url 'substitution_user_turn_off' %}">{{ request.user.username }} [{{ real_user.username }}]</a>
{% else %}
    <a href="{% url 'logout' %}">{{ request.user.username }}</a>
{% endif %}
```

## TODO
- Python 3 support


## License
django-substitute-user is released under the MIT License. See the LICENSE file for more details.
