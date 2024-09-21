from django.contrib import admin
from django.urls import path, include
from escola.views import StudentViewSet, CourseViewSet, RegistrationViewSet, ListRegistrationStudent, ListRegistrationCourse
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'registrations', RegistrationViewSet, basename='registration')



schema_view = get_schema_view(
   openapi.Info(
      title="Documentação da API",
      default_version='v1',
      description="Doc da API Escola",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/registrations/', ListRegistrationStudent.as_view()),
    path('courses/<int:pk>/registrations/', ListRegistrationCourse.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
