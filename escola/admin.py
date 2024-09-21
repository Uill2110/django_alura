from django.contrib import admin
from escola.models import Student, Course, Registration


class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'date_birth', 'cpf', 'mobile_number',)
    list_display_links = ('id', 'name',)
    list_per_page = 20
    search_fields = ('name','cpf')
    
admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_code', 'description',)
    list_display_links = ('id', 'course_code',)
    search_fields = ('course_code',)
    
admin.site.register(Course, Courses)

class Registrations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'turn',)
    list_display_links = ('id',)
    
admin.site.register(Registration, Registrations)

