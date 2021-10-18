from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, user_name, email, password=None, **extra_fields):

        if not email:
            raise ValueError('email is must')

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, user_name='',):
        user = self.create_user(user_name, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    user_name = models.CharField(
        'user_name',
        max_length=150,
        blank=True,
        null=True,
        unique=True,
    )
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.email
