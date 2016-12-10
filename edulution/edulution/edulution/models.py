from django.db import models


class User(models.Model):
    username = models.CharField()


# like maths, literature
class Subject(models.Model):
    name = models.CharField()

