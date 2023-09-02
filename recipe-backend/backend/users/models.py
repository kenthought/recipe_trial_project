from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(
        self,
        email,
        password,
        first_name,
        middle_name,
        last_name,
        **extra_fields
    ):
        if not email:
            raise ValueError("Email is Required")
        user = self.model(
            email=email,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        password,
        first_name,
        middle_name,
        last_name,
        **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")

        return self.create_user(
            email,
            password,
            first_name,
            middle_name,
            last_name,
            **extra_fields
        )


class UserData(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [ "first_name", "middle_name", "last_name"]

    def __str__(self):
        return self.email
