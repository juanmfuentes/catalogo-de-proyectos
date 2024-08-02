from django.contrib import admin
from .models import User, Administrador, Alumno, Empresa, ProgramaEducativo, Proceso, Proyecto, ProyectoAlumno, ConfiguracionPaginas

# Register your models here.
admin.site.register(User)
admin.site.register(Administrador)
admin.site.register(Alumno)
admin.site.register(Empresa)
admin.site.register(ProgramaEducativo)
admin.site.register(Proceso)
admin.site.register(Proyecto)
admin.site.register(ProyectoAlumno)
admin.site.register(ConfiguracionPaginas)