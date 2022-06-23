from rest_framework import viewsets, generics, status
from course.models import Course
from course.serializer import CourseSerializer, ListCourseRegistrationsSerializer
from registration.models import Registration
from rest_framework.response import Response
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
# from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class CourseViewSet(viewsets.ModelViewSet):
    """ Show all courses """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # Default methods to ModelViewSet
    http_method_names = ['get', 'post', 'put', 'patch']

    # Passed in core.settings.py by default
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]

    # Redefining create method
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            
            # Add Location to response header with our api path
            response['Location'] = request.build_absolute_uri() + id

            return response

class ListCourseRegistrationsViewSet(generics.ListAPIView):
    """ Show all students registrated in course """
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListCourseRegistrationsSerializer

    # Passed in core.settings.py by default
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
