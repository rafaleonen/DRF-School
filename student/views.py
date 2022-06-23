from rest_framework import viewsets, generics
from student.models import Student
from student.serializer import StudentSerializer, ListStudentRegistrationsSerializer, StudentSerializerV2
from registration.models import Registration
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
# from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class StudentViewSet(viewsets.ModelViewSet):
    """ Show all students """
    queryset = Student.objects.all()

    # Passed in core.settings.py by default
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]

    # Default methods to ModelViewSet
    # http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    serializer_class = StudentSerializer
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer

class ListStudentRegistrationsViewSet(generics.ListAPIView):
    """ List all registrations done by student """
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentRegistrationsSerializer

    # Passed in core.settings.py by default
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]