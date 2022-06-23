from django.contrib import admin
from registration.models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id',)
    search_fields = ('period',)
    list_per_page = 10

admin.site.register(Registration, RegistrationAdmin)
