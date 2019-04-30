import logging

from user.models import UserProfile
from django.contrib.auth.models import User


class CustomAuthenticationBackend:
    """
    Custom authentication class. Allows users to log in with email as well as
    adds company alias to authentication
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Custom implementation of the authenticate function
        """
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username)
            except User.MultipleObjectsReturned:
                logging.error("Multiple users were returned for {}".format(username))
                return None
            except User.DoesNotExist:
                logging.fatal("User with the username {} doesn't exist".format(username))
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
        """
        Returns User object
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
