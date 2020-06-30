from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return '{}'.format(self.email)
class Questions(models.Model):
    questiontext = models.CharField(max_length=200)

    def __str__(self):
        return self.questiontext

class QuestionFeedback(models.Model):
    questions = models.ForeignKey(Questions, default=1, verbose_name="Questions", on_delete=models.SET_DEFAULT)
    feedback = models.CharField(max_length=200)
    timestamp= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.questions.questiontext
