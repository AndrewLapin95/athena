from django.contrib.auth.models import User
from django.core.exceptions import FieldError

from user.models import UserProfile


class CustomAuthenticationBackend:
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username)
            except User.MultipleObjectsReturned:
                return None
            except User.DoesNotExist:
                return None

        if not user.is_superuser:
                form_alias = request.POST.get("alias")
                if form_alias == "" or form_alias is None:
                    return None

                alias = UserProfile.objects.get(user_id=user.id).company_alias
                if getattr(user, 'is_active') and user.check_password(password) and alias == form_alias:
                    return user
        else:
            if getattr(user, 'is_active') and user.check_password(password):
                return user

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None