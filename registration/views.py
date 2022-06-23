from rest_framework import viewsets
from registration.models import Registration
from registration.serializer import RegistrationSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
# from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class RegistrationViewSet(viewsets.ModelViewSet):
    """ Show all registrations """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    # Passed in core.settings.py by default
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]

    # This method create a cache and reload each 20sec
    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(RegistrationViewSet, self).dispatch(*args, **kwargs)
    
