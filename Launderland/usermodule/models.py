from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, mobile, password, **extra_fields):
        if not mobile:
            raise ValueError('The given mobile must be set')
        # mobile = self.mobile
        user = self.model(mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(mobile, password, **extra_fields)

    def create_superuser(self, mobile, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(mobile, password, **extra_fields)


class User(AbstractUser):
    username = None
    mobile = models.CharField(unique=True, max_length=10)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=15)
    profile_pic = models.ImageField(default="profile.png", blank=True)
    gender_choice = (('Male', 'Male'), ('Female', 'Female'),
                     ('Other', 'Other'))
    gender = models.CharField(max_length=7, choices=gender_choice)
    user_type_choice = ((1, 'Owner'), (2, 'Staff'), (3, 'Customer'))
    user_type = models.PositiveSmallIntegerField(
        choices=user_type_choice)
    staff_status = models.BooleanField(default=False)
    address = models.CharField(max_length=100)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    creation_date = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.last_name + ", " + self.first_name
