from django.db import models
from jsonfield import JSONField
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class idModel(models.Model):
    invalid_trigger = models.CharField(max_length=50)
    key = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    reuse = models.BooleanField(default=True)
    support_multiple=models.BooleanField(default=True)
    pick_first=models.BooleanField(default=False)
    support_values=ArrayField(models.CharField(max_length=50, blank=True), size = 8)
    type1 = ArrayField(models.CharField(max_length=50,default="id"), size=8, default=list)
    validation_parser = models.CharField(max_length=50)
    values= ArrayField(JSONField(null=True, blank=True, default=dict), max_length=200,
    blank=True, default=list)
    
class ageModel(models.Model):
    invalid_trigger = models.CharField(max_length=50)
    key = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    reuse = models.BooleanField(default=True)
    constraint=models.CharField(max_length=250)
    support_multiple=models.BooleanField(default=True)
    pick_first=models.BooleanField(default=False)
    var_name=models.CharField(max_length=20)
    type1 = ArrayField(models.CharField(max_length=50,default="id"), size=8, default=list)
    validation_parser = models.CharField(max_length=50)
    values= ArrayField(JSONField(null=True, blank=True, default=dict), max_length=200, 
    blank=True, default=list)
        