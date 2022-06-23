from django.contrib import admin
from course.models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_code', 'title', 'level')
    list_display_links = ('id', 'course_code', 'title')
    search_fields = ('course_code', 'title')
    list_per_page = 10

admin.site.register(Course, CourseAdmin)
