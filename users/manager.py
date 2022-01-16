from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, department_id=None, password=None):
        """
        Creates and saves a User with the given email, firstname, lastname, department_id and password.
        """
        if not email:
            raise ValueError('Users must have an email address')


        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.fname = firstname
        user.lname = lastname
        user.department = department_id
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, firstname, lastname, department_id):
        """
        Creates and saves a User with the given email, firstname, lastname, department_id and password.
        """
        user = self.create_user(
            email,
            firstname,
            lastname,
            department_id,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
