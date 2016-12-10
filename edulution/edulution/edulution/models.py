from django.db import models


# like addition or subtraction
# Note : you can deduce the number of modules linked by doing a search query
class Module(models.Model):
    name = models.CharField(max_length=255)
    requirement = models.PositiveIntegerField() # the module "2" needs "1" to be started
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)


class Exercise(models.Model):
    difficulty = models.PositiveIntegerField()
    exo_id = models.CharField(max_length=255, primary_key=True)
    module = models.ForeignKey('Module', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    path = models.TextField()


class Student(models.Model):
    username = models.CharField(max_length=255, unique=True)
    user_id = models.CharField(max_length=255, primary_key=True)
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


class LogExercise(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exo = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    nb_attempts = models.PositiveIntegerField()
    struggling = models.BooleanField()
    date_completed = models.DateField()
    percentage_of_questions_passed = models.FloatField()
    nb_attempts_before_completion = models.PositiveIntegerField()


# like maths, literature
class Subject(models.Model):
    name = models.CharField(max_length=255)


class Test(models.Model):
    module = models.OneToOneField(Module, related_name='associated_test')


class Question(models.Model):
    test = models.ForeignKey('Test', on_delete=models.CASCADE)
    question = models.TextField()
    list_answer = models.TextField(null=True, blank=True) # optional JSON-encoded list
    answer = models.CharField(max_length=255)                           # response of the question

