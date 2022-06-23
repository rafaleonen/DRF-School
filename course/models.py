from django.db import models

class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediary'),
        ('A', 'Advanced')
    )

    course_code = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.title
