from django.db import models

# Create your models here.
class Jdata(models.Model):
    userId = models.IntegerField()
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=400)

    class Meta:
        db_table = 'jdata'
        managed = True