from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = "users"


class Resources(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, unique=True)
    available = models.BooleanField(default=True)

    class Meta:
        db_table = "resources"


class ResourceScheduling(models.Model):
    id = models.AutoField(primary_key=True)
    resource = models.ForeignKey(Resources, on_delete=models.DO_NOTHING)
    initial_date = models.DateTimeField()
    final_date = models.DateTimeField()
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "resource_scheduling"
