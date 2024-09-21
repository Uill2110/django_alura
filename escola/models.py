from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank= False)
    cpf = models.CharField(max_length=11, unique=True)
    date_birth = models.DateField()
    mobile_number = models.CharField(max_length=14)
    
    def __str__(self):
        return self.name
    
    
class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )
    course_code = models.CharField(max_length=10, unique=False, validators=[MinLengthValidator(3)])
    description = models.CharField(max_length=100,blank= False)
    level = models.CharField(blank= False, null= False, max_length=100, choices= LEVEL, default='B')

    def __str__(self):
        return self.course_code
    
class Registration(models.Model):
    TURN = (
        ('B', 'Morning'),
        ('I', 'Afternoon'),
        ('N', 'Night'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    turn = models.CharField(blank= False, null= False, max_length=100, choices= TURN, default='B')
    