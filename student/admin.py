from django.contrib import admin
from student.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf', 'rg', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Student, StudentAdmin)
