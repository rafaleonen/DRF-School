from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()
    phone = models.CharField(max_length=11, default='')
    photo = models.ImageField(blank=True, )

    def __str__(self):
        return self.name