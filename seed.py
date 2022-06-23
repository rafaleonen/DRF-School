import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from course.models import  Course
from student.models import Student

def create_students(quantity):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantity):
        cpf = CPF()
        name = fake.name()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
        cpf = cpf.generate()
        birth_date = fake.date_between(start_date='-18y', end_date='today')
        new_student = Student(name=name,rg=rg, cpf=cpf,birth_date=birth_date)
        new_student.save()

def create_courses(quantity):
    Faker.seed(10)
    for _ in range(quantity):
        course_code = "{}{}-{}".format(random.choice("ABCDEF"), random.randrange(10, 99),random.randrange(1, 9))
        titles = ['Python Fundamentos', 'Python intermediário','Python Avançado', 'Python para Data Science', 'Python/React']
        title = random.choice(titles)
        titles.remove(title)
        description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        level = random.choice("BIA")
        new_course = Course(course_code=course_code,title=title, description=description, level=level)
        new_course.save()


create_students(200)
create_courses(5)