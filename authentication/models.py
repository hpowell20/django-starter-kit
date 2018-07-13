from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    User profile model used in the system with the same behavior Abstract User with the same behaviour as
    Django's default User.  This model does not have a username field and uses email as the
    USERNAME_FIELD for authentication.
    The following attributes are inherited from the AbstractBaseUser superclass:
       * password
       * last_login
    The following permissions are inherited from PermissionMixin superclass:
        * is_superuser
        * groups
        * user_permissions
    """
    email = models.EmailField('Email Address', max_length=254, unique=True, db_index=True)
    first_name = models.CharField('First Name', max_length=30, blank=True)
    last_name = models.CharField('Last Name', max_length=30, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_staff = models.BooleanField(_('Staff Status'), default=False, help_text=_(
        'Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('Active'), default=True, help_text=_(
        'Designates whether this user should be treated as '
        'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('pk',)

    def get_full_name(self):
        """ Returns the first_name plus the last_name, with a space in between. """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """ Returns the short name for the user. """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """ Send an email to this User."""
        send_mail(subject, message, from_email, [self.email], **kwargs)