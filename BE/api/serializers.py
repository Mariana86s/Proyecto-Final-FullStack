from rest_framework.serializers import ModelSerializer
from .models import Usuario

from rest_framework import serializers
from .models import (
    Usuario, Rol, Curso, Instructor, Inscripcion,
    Evento, CategoriaEvento, AsistenteEvento,
    Noticia, MensajeContacto
)
from django.contrib.auth.hashers import make_password


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    rol = RolSerializer(read_only=True)
    rol_id = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all(), source='rol', write_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'correo', 'telefono', 'direccion', 'rol', 'rol_id']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'correo', 'contrasena']
        extra_kwargs = {'contrasena': {'write_only': True}}

    def create(self, validated_data):
        validated_data['contrasena'] = make_password(validated_data['contrasena'])
        return Usuario.objects.create(**validated_data)


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only=True)
    instructor_id = serializers.PrimaryKeyRelatedField(
        queryset=Instructor.objects.all(), source='instructor', write_only=True
    )

    class Meta:
        model = Curso
        fields = '__all__'


class InscripcionSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    curso = CursoSerializer(read_only=True)

    class Meta:
        model = Inscripcion
        fields = '__all__'


class CategoriaEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaEvento
        fields = '__all__'


class EventoSerializer(serializers.ModelSerializer):
    organizador = UsuarioSerializer(read_only=True)
    categoria = CategoriaEventoSerializer(read_only=True)

    class Meta:
        model = Evento
        fields = '__all__'


class NoticiaSerializer(serializers.ModelSerializer):
    autor = UsuarioSerializer(read_only=True)

    class Meta:
        model = Noticia
        fields = '__all__'


class MensajeContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MensajeContacto
        fields = '__all__'
