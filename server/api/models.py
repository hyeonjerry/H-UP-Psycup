from django.db import models
from django.utils import timezone


class Test(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions',
                             on_delete=models.CASCADE)
    question = models.CharField(max_length=256)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=64)
    score = models.IntegerField()

    def __str__(self):
        return self.answer


class Result(models.Model):
    test = models.ForeignKey(Test, related_name='results',
                             on_delete=models.CASCADE)
    result = models.CharField(max_length=256)
    lower = models.IntegerField()
    upper = models.IntegerField()

    def __str__(self):
        return self.result
