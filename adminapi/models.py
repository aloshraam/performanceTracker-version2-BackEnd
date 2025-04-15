from django.db import models
from django.contrib.auth import get_user_model
from datetime import time

User = get_user_model()

class Attendance(models.Model):
    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Late', 'Late'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    login_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.status}"