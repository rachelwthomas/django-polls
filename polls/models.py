import datetime

from django.db import models
from django.utils import timezone

# Each field is represented by an instance of a Field class – e.g.,
# CharField for character fields and DateTimeField for datetimes.
# This tells Django what type of data each field holds.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #add so text is human readable
    def __str__(self):
        return self.question_text

# Question.was_published_recently() should return False if its pub_date is in the future.
#  Amend the method in models.py,
# so that it will only return True if the date is also in the past:
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    #add so text is human readable
    def __str__(self):
        return self.choice_text
