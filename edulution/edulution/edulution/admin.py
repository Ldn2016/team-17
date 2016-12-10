from django.contrib import admin
from .models import *


class ModuleAdmin(admin.ModelAdmin):
    pass


class ExerciseAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


class StudentModuleAdmin(admin.ModelAdmin):
    pass


class LogExerciseAdmin(admin.ModelAdmin):
    pass


class SubjectAdmin(admin.ModelAdmin):
    pass


class TestAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Module, ModuleAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentModule, StudentModuleAdmin)
admin.site.register(LogExercise, LogExerciseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
