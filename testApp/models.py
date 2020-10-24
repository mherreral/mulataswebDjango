from django.db import models

class Quiz(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)


class Grade(models.Model):
    score = models.IntegerField(default=0)
