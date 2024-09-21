from rest_framework import serializers
from escola.models import Student, Course, Registration
from escola.validators import invalid_cpf, invalid_mobile_number, invalid_name

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'cpf', 'date_birth', 'mobile_number']
    def validate(self, dados):
        if invalid_cpf:
            raise serializers.ValidationError({'cpf':'O CPF deve ter um valor válido.'})
        if invalid_name:
            raise serializers.ValidationError({'name':'O nome só pode ter letras'})
        if invalid_mobile_number:
            raise serializers.ValidationError({'mobile_number':'O celular precisa seguir o modelo: 86 99999-9999 (respeitando traços e espaços).'})
        return dados
    
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
        
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        exclude = []       

class ListRegistrationStudentSerializers(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    turn = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        fields = ['course', 'turn']
    def get_turn(self, obj):
        return obj.get_turn_display()
    
class ListRegistrationCourseSerializers(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Registration
        fields = ['student_name']
    
    
class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'mobile_number']
        
    def validate(self, dados):
        if invalid_name:
            raise serializers.ValidationError({'name':'O nome só pode ter letras'})
        if invalid_mobile_number:
            raise serializers.ValidationError({'mobile_number':'O celular precisa seguir o modelo: 86 99999-9999 (respeitando traços e espaços).'})
        return dados