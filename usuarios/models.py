from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    es_administrador = models.BooleanField('Administrador', default=False)
    es_alumno = models.BooleanField('Alumno', default=False)
    es_empresa = models.BooleanField('Empresa', default=False)


class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class ProgramaEducativo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.IntegerField()
    nombre = models.CharField(max_length=50, default="")
    apellido_paterno = models.CharField(max_length=50, default="")
    apellido_materno = models.CharField(max_length=50, default="")
    sexo = models.CharField(max_length=20, default="")
    correo_personal = models.EmailField(max_length=80, default="")
    correo_institucional = models.EmailField(max_length=80, default="")
    telefono = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    programa_educativo = models.ForeignKey(ProgramaEducativo, on_delete=models.CASCADE)
    proyectos = models.ManyToManyField('Proyecto', through='ProyectoAlumno')

    def __str__(self):
        return str(self.matricula)


class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    razon_social = models.CharField(max_length=100)
    rfc = models.CharField(max_length=20)
    telefono_empresa = models.CharField(max_length=20)
    titular = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    nombre_enlace = models.CharField(max_length=100)
    telefono_enlace = models.CharField(max_length=20)
    correo_enlace = models.EmailField(max_length=100)
    correo = models.EmailField(max_length=100)
    is_active = models.BooleanField(default=True)
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    colonia = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    entidad = models.CharField(max_length=100)

    def __str__(self):
        return self.razon_social


class Proceso(models.Model):
    id_proceso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    PERIODO_CHOICES = [
        ('', 'Selecciona una opción'),
        ('Enero-Abril', 'Enero-Abril'),
        ('Mayo-Agosto', 'Mayo-Agosto'),
        ('Septiembre-Diciembre', 'Septiembre-Diciembre'),
    ]

    MODALIDAD_CHOICES = [
        ('', 'Selecciona una opción'),
        ('Presencial', 'Presencial'),
        ('Remoto', 'Remoto'),
        ('Mixta', 'Mixta'),
    ]
    
    periodo = models.CharField(max_length=25, choices=PERIODO_CHOICES)
    año = models.IntegerField()
    vacantes = models.IntegerField()
    vacantes_disponibles = models.IntegerField()
    modalidad = models.CharField(max_length=10, choices=MODALIDAD_CHOICES)
    nombre = models.CharField(max_length=100)
    objetivo = models.TextField()
    justificacion = models.TextField()
    asesor = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    id_programa_educativo = models.ForeignKey(ProgramaEducativo, on_delete=models.CASCADE)
    id_proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    alumnos = models.ManyToManyField(Alumno, through='ProyectoAlumno')

    def __str__(self):
        return self.nombre
    
class ProyectoAlumno(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.alumno.user.username} - {self.proyecto.nombre}"
    
class ConfiguracionPaginas(models.Model):
    estado_paginas_alumnos = models.BooleanField(default=True)
    estado_paginas_empresas = models.BooleanField(default=True)
    

