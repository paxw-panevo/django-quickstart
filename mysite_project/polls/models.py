from datetime import timedelta

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f"({self.pk}) {self.question_text}"

    # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/
    # #django.contrib.admin.ModelAdmin.list_display
    # `boolean` - Allows Django to display pretty yes, no, unknown icons
    # `description` - Allows user to provide a human-friendlier column name
    # `ordering` - Specifies which database field can be used to sort this
    #   column (which is not a database field itself).
    #     > Usually, elements of list_display that aren’t actual database fields
    #     can’t be used in sorting (because Django does all the sorting at the
    #     database level).
    #     > However, if an element of list_display represents a certain database
    #     field, you can indicate this fact by using the `ordering` argument
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self) -> bool:
        DATETIME_NOW = timezone.now()
        the_day_before = DATETIME_NOW - timedelta(days=1)
        return DATETIME_NOW >= self.pub_date >= the_day_before

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"({self.pk}) {self.choice_text}: {self.votes}"
