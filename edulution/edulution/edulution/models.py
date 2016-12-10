from django.db import models


class User(models.Model):
    username = models.CharField()


# like maths, literature
class Subject(models.Model):
    name = models.CharField()


class Module(models.Model):
    name = models.CharField()
    requirement = models.PositiveIntegerField() # the module "2" needs "1" to be started
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)

