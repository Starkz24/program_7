from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    usn = models.CharField(max_length=20)
    semester = models.IntegerField()
    fee_paid = models.BooleanField()

    def __str__(self):
        return self.name