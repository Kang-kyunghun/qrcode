from django.db import models

class Attendent(models.Model):
    name         = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email        = models.CharField(max_length=100)
    storage_key  = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'attendents'
