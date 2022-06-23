from django.db import models
from student.models import Student
from course.models import Course

class Registration(models.Model):
    PERIOD = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Night')
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=1, choices=PERIOD, blank=False, null= False, default='M')

    def __str__(self):
        return f'{self.student} in {self.course}'