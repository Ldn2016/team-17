# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 03:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('difficulty', models.PositiveIntegerField()),
                ('exo_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LogExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_attempts', models.PositiveIntegerField()),
                ('struggling', models.BooleanField()),
                ('date_completed', models.DateField()),
                ('percentage_of_questions_passed', models.FloatField()),
                ('nb_attempts_before_completion', models.PositiveIntegerField()),
                ('exo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edulution.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('requirement', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('list_answer', models.TextField(blank=True, null=True)),
                ('answer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StudentModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_exo_succeded', models.PositiveIntegerField()),
                ('status', models.PositiveIntegerField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edulution.Module')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edulution.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='associated_test', to='edulution.Module')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='modules',
            field=models.ManyToManyField(through='edulution.StudentModule', to='edulution.Module'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edulution.Test'),
        ),
        migrations.AddField(
            model_name='module',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edulution.Subject'),
        ),
        migrations.AddField(
            model_name='logexercise',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edulution.Student'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edulution.Module'),
        ),
    ]
