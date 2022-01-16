from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager

class Department(models.Model):
    department_id = models.CharField(verbose_name='Abteilung_kz', primary_key=True, max_length=2, default='IT')
    department_name = models.CharField(verbose_name='Abteilung', blank=False, null=False, max_length=255, default='Informational Technologies')

    class Meta:
        ordering = ['department_id']

    def __str__(self):
        return f'{self.department_id} | {self.department_name}'

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    fname = models.CharField(verbose_name='Vorname', max_length=255)
    lname = models.CharField(verbose_name='Nachname', max_length=255)
    department = models.ForeignKey(to=Department, verbose_name='Abteilung_kz', on_delete=models.RESTRICT, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_superuser(self):
        "Is the user a admin member?"
        return self.admin


