from rest_framework import serializers
from student.models import Student
from registration.models import Registration

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['phone']

class ListStudentRegistrationsSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.title')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        exclude = ['student']
    
    def get_period(self, obj):
        return obj.get_period_display()

class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'