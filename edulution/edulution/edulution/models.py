from django.db import models


class User(models.Model):
    username = models.CharField()


# like maths, literature
class Subject(models.Model):
    name = models.CharField()


# like addition or subtraction
class Module(models.Model):
    name = models.CharField()
    requirement = models.PositiveIntegerField() # the module "2" needs "1" to be started
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)


class Exercise(models.Model):
    difficulty = models.PositiveIntegerField()
    exo_id = models.CharField(primary_key=True)
    module = models.ForeignKey('Module', on_delete=models.CASCADE)
    title = models.CharField()
    path = models.TextField()


class Test(models.Model):
    module = models.OneToOneField(Module, related_name='associated_test')

