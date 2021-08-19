from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Url(models.Model):
    long = models.URLField(blank= True , null= True , max_length= 500)
    short = models.URLField(blank= True , null= True)
    visit_number = models.BigIntegerField(default =1 )

