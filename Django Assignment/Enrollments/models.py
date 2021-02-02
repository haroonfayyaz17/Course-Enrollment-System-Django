from Students.models import Student
from Courses.models import Course
from django.db import models


# Create your models here.


class Enrollment(models.Model):

    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    grade = models.CharField(max_length=2)
