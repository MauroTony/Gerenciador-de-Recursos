from django.db import models


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = "users"


class Resources(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.IntegerField(unique=True)
    available = models.BooleanField(default=True)

    class Meta:
        db_table = "resources"


class ResourceScheduling(models.Model):
    id = models.AutoField(primary_key=True)
    resource = models.ForeignKey(Resources, on_delete=models.DO_NOTHING)
    initial_date = models.DateTimeField()
    final_date = models.DateTimeField()
    user = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "resource_scheduling"
