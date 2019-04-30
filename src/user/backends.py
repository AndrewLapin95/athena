from django.contrib.auth.models import User
from django.core.exceptions import FieldError

from user.models import UserProfile


class CustomAuthenticationBackend:
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        
        form_alias = request.POST.get("alias")
        if form_alias == "" or form_alias is None:
            return None

        try:
            user = User.objects.get(username=username)
            alias = UserProfile.objects.get(user_id=user.id).company_alias
            if getattr(user, 'is_active') and user.check_password(password) and alias == form_alias:
                return user
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username)
                alias = UserProfile.objects.get(user_id=user.id).company_alias
                if getattr(user, 'is_active') and user.check_password(password) and alias == form_alias:
                    return user
            except User.MultipleObjectsReturned:
                return None
            except User.DoesNotExist:
                return None

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None