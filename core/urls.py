
from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from student.views import StudentViewSet, ListStudentRegistrationsViewSet
from course.views import CourseViewSet, ListCourseRegistrationsViewSet
from registration.views import RegistrationViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename="Student")
router.register('courses', CourseViewSet, basename="Courses")
router.register('registrations', RegistrationViewSet, basename="Registrations")

urlpatterns = [
    path('admin/', include('admin_honeypot.urls')),
    path('dashboard-admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('students/<int:pk>/registrations/', ListStudentRegistrationsViewSet.as_view()),
    path('courses/<int:pk>/registrations/', ListCourseRegistrationsViewSet.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
