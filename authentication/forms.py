from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authentication.models import User


class UserProfileCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and password
    """
    def __init__(self, *args, **kargs):
        super(UserProfileCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = User
        fields = ("email",)


class UserProfileChangeForm(UserChangeForm):
    """
    A form for updating users which includes all the fields for the but replaces the password field
    with admin's password hash display field.
    """
    def __init__(self, *args, **kargs):
        super(UserProfileChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = User
        fields = ("email",)
