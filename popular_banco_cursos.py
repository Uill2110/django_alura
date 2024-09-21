import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from escola.models import Course

dados = [
    ('AD113', 'Curso de Python Orientação à Objetos 01'),
    ('AD112', 'Curso de Python Orientação à Objetos 02'),
    ('AD113', 'Curso de Python Orientação à Objetos 03'),
    ('AD114', 'Curso de Python Orientação à Objetos 04'),
    ('AD115', 'Curso de Python Orientação à Objetos 05'),
    ('ABJ11', 'Curso de Django 01'),
    ('ABJ12', 'Curso de Django 02'),
    ('ABJ13', 'Curso de Django 03'),
    ('ABJ14', 'Curso de Django 04'),
    ('ABJ15', 'Curso de Django 05'),
    ('ABJ16', 'Curso de Django 06'),
    ('ABJR101', 'Curso de Django REST Framework 01'),
    ('ABJR102', 'Curso de Django REST Framework 02'),
    ('ABJR103', 'Curso de Django REST Framework 03'),
    ('ABJR104', 'Curso de Django REST Framework 04'),
    ('ABJR105', 'Curso de Django REST Framework 05'),
    ('ABJR106', 'Curso de Django REST Framework 06')
]

niveis = ['B', 'I', 'A']

def criar_cursos():
    for codigo, descricao in dados:
        nivel = random.choice(niveis)
        Course.objects.create(course_code=codigo, description=descricao, level=nivel)
criar_cursos()