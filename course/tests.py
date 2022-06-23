from rest_framework.test import APITestCase
from rest_framework import status
from course.models import Course
from django.urls import reverse

class CourseTestCase(APITestCase):

    # To pass in testes it'll need to comment permissions
    def setUp(self):
        self.list_url = reverse('Courses-list')  # route basename
        self.curso_1 = Course.objects.create(
            course_code='CTT1',
            title='Course Test 1',
            description='Description Test',
            level='B'
        )
        self.curso_2 = Course.objects.create(
            course_code='CTT2',
            title='Course Test 2',
            description='Description Test',
            level='A'
        )

    def test_list_course(self):
        """ Test to list course """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        """ Test to create a course """
        data = {
            'course_code': 'CTT3',
            'title': 'Course Test 3',
            'description': 'Description Test',
            'level': 'I'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_course(self):
        """  Test to update entire course """
        data = {
            'course_code': 'CTT3',
            'title': 'Course Test 3',
            'description': 'Description Test',
            'level': 'I'
        }

        response = self.client.put('/courses/2/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_course_field(self):
        """  Test to update entire course """
        data = {
            'description': 'Updating description test',
        }

        response = self.client.patch('/courses/2/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_course(self):
        """ Test to check if is really not possible to delete a course """
        response = self.client.delete('/courses/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
