from rest_framework import serializers
from registration.models import Registration
from course.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ListCourseRegistrationsSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Registration
        fields = ['student_name']

    def get_period(self, obj):
        return obj.get_period_display()