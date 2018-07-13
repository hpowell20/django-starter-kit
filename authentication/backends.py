from authentication.models import User


class EmailAuthBackend(object):
    """
    A custom authentication backend. Allows users to log in using their email address.
    """
    @staticmethod
    def authenticate(email=None, password=None):
        """
        Authentication method
        """
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None

