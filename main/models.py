from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Property(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)


class Entity(models.Model):
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()
    properties = models.ManyToManyField(Property)
