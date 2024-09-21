from escola.models import Student, Course, Registration
from escola.serializers import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationStudentSerializers, ListRegistrationCourseSerializers, StudentSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from escola.throttles import RegistrationAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class StudentViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for viewing and managing students.

    Attributes:
    - queryset: A queryset of all students, ordered by their IDs.
    - filter_backends: A list of filter backends, including DjangoFilterBackend, SearchFilter, and OrderingFilter.
    - ordering_fields: A list of fields that can be used for ordering, currently only 'name'.
    - search_fields: A list of fields that can be used for searching, currently only 'cpf'.

    Methods:
    - get_serializer_class: Returns the serializer class based on the API version.
        - If the API version is 'v2', returns StudentSerializerV2.
        - Otherwise, returns StudentSerializer.
    '''
    queryset = Student.objects.all().order_by('id')
    # serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name']
    search_fields = ['cpf']
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer
        
# class CourseViewSet(viewsets.ModelViewSet):
#     '''
#     API endpoint for viewing and managing courses.

#     Attributes:
#     - queryset: A queryset of all courses, ordered by their IDs.
#     - serializer_class: CourseSerializer
#     '''
#     search_fields = ['course_code']    
#     queryset = Course.objects.all().order_by('id')
#     serializer_class = CourseSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

class CourseViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de courses.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Course.objects.all().order_by("id")
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RegistrationViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for viewing and managing registrations.

    Attributes:
    - queryset: A queryset of all registrations, ordered by their IDs.
    - serializer_class: RegistrationSerializer
    - throttle_classes: A list of throttle classes, including UserRateThrottle and RegistrationAnonRateThrottle.
    - http_method_names: A list of allowed HTTP methods, currently only 'get' and 'post'.
    '''
    queryset = Registration.objects.all().order_by('id')
    serializer_class = RegistrationSerializer
    throttle_classes = [UserRateThrottle, RegistrationAnonRateThrottle]
    http_method_names = ['get', 'post']
    
class ListRegistrationStudent(generics.ListAPIView):
    '''
    Descrição da View:
    - Lista Matriculas por id de Student
    Attributes:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    '''
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListRegistrationStudentSerializers
    
class ListRegistrationCourse(generics.ListAPIView):
    '''
    Descrição da View:
    - Lista Matriculas por id de Course
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    '''
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListRegistrationCourseSerializers