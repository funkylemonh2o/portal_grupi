from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'user'}
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.grade}"
