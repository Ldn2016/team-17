from django.db import models


class Student(models.Model):
    username = models.CharField()
    modules = models.ManyToManyField(
        Module,
        through='StudentModule',
        through_fields=('student', 'module'),
    )


class StudentModule(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    nb_exo_succeded = models.PositiveIntegerField()
    status = models.PositiveIntegerField() # number of times the student passed the test associated with the module


# like maths, literature
class Subject(models.Model):
    name = models.CharField()


# like addition or subtraction
# Note : you can deduce the number of modules linked by doing a search query
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


class Question(models.Model):
    test = models.ForeignKey('Test', on_delete=models.CASCADE)
    question = models.TextField()
    list_answer = models.TextField() # JSON-encoded list
    answer = models.IntegerField()   # index of the answer in the JSON encoded-list

