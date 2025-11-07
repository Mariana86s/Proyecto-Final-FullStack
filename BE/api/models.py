from django.db import models

# =============================
#  Roles
# =============================
class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre


# =============================
#  Usuarios
# =============================
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, related_name='usuarios')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# =============================
#  Instructores
# =============================
class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# =============================
#  Cursos
# =============================
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    nivel = models.CharField(max_length=50, blank=True, null=True)
    duracion = models.PositiveIntegerField(help_text="Duración en horas", blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, related_name='cursos')

    def __str__(self):
        return self.nombre


# =============================
#  Inscripciones
# =============================
class Inscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return f"{self.usuario} - {self.curso}"


# =============================
#  Categorías de Eventos
# =============================
class CategoriaEvento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


# =============================
#  Eventos
# =============================
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_evento = models.DateField(blank=True, null=True)
    hora_evento = models.TimeField(blank=True, null=True)
    lugar = models.CharField(max_length=100, blank=True, null=True)
    organizador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='eventos_organizados')
    categoria = models.ForeignKey(CategoriaEvento, on_delete=models.SET_NULL, null=True, related_name='eventos')

    def __str__(self):
        return self.titulo


# =============================
#  Asistentes a Evento (N:M)
# =============================
class AsistenteEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='asistentes')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos_asistidos')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} -> {self.evento}"


# =============================
#  Noticias
# =============================
class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='noticias')

    def __str__(self):
        return self.titulo


# =============================
#  Mensajes de Contacto
# =============================
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    asunto = models.CharField(max_length=150, blank=True, null=True)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre}"