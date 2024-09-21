# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from escola.models import Student, Course, Registration
from escola.serializers import StudentSerializer, CourseSerializer, RegistrationSerializer
from django.contrib.auth.models import User

class TestModels(TestCase):
    def test_student_model(self):
        student = Student.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            cpf='12345678910',
            date_birth='1990-01-01',
            mobile_number='1234567890'
        )
        self.assertEqual(student.name, 'John Doe')

    def test_course_model(self):
        course = Course.objects.create(
            course_code='C001',
            description='Course 1',
            level='B'
        )
        self.assertEqual(course.course_code, 'C001')

    def test_registration_model(self):
        student = Student.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            cpf='12345678910',
            date_birth='1990-01-01',
            mobile_number='1234567890'
        )
        course = Course.objects.create(
            course_code='C001',
            description='Course 1',
            level='B'
        )
        registration = Registration.objects.create(
            student=student,
            course=course,
            turn='B'
        )
        self.assertEqual(registration.student, student)

class TestSerializers(TestCase):
    def test_student_serializer(self):
        student = Student.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            cpf='12345678910',
            date_birth='1990-01-01',
            mobile_number='1234567890'
        )
        serializer = StudentSerializer(student)
        self.assertEqual(serializer.data['name'], 'John Doe')

    def test_course_serializer(self):
        course = Course.objects.create(
            course_code='C001',
            description='Course 1',
            level='B'
        )
        serializer = CourseSerializer(course)
        self.assertEqual(serializer.data['course_code'], 'C001')

    def test_registration_serializer(self):
        student = Student.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            cpf='12345678910',
            date_birth='1990-01-01',
            mobile_number='1234567890'
        )
        course = Course.objects.create(
            course_code='C001',
            description='Course 1',
            level='B'
        )
        registration = Registration.objects.create(
            student=student,
            course=course,
            turn='B'
        )
        serializer = RegistrationSerializer(registration)
        self.assertEqual(serializer.data['student'], student.id)

class TestViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password')
        self.client.force_authenticate(user=self.user)
        
    def test_student_viewset(self):
        response = self.client.get(reverse('student-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_viewset(self):
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_registration_viewset(self):
        response = self.client.get(reverse('registration-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_list_registration_student(self):
    #     student = Student.objects.create(
    #         name='John Doe',
    #         email='johndoe@example.com',
    #         cpf='12345678910',
    #         date_birth='1990-01-01',
    #         mobile_number='1234567890'
    #     )
    #     response = self.client.get(reverse('course', args=[student.id]))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_list_registration_course(self):
    #     course = Course.objects.create(
    #         code='C001',
    #         description='Course 1',
    #         level='B'
    #     )
    #     response = self.client.get(reverse('student', args=[course.id]))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)