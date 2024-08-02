from django.urls import path
from . import views

urlpatterns = [
    #
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('controlar_paginas/', views.controlar_paginas, name='controlar_paginas'),
    path('pagina_desactivada/', views.pagina_desactivada, name='pagina_desactivada'),
    path('proyecto/pdf/<int:proyecto_id>/', views.descargar_proyecto_pdf, name='descargar_proyecto_pdf'),

    # alumnos
    path('registro/alumno/', views.registro_alumno, name='registro_alumno'),
    path('alumno/home', views.alumno_home, name='alumno_home'),
    path('alumno/perfil', views.alumno_perfil, name='alumno_perfil'),
    path('alumno/catalogo', views.alumno_catalogo, name='alumno_catalogo'),
    path('alumno/proyecto', views.alumno_proyecto, name='alumno_proyecto'),
    path('alumno/seleccionar_proyecto/<int:proyecto_id>/', views.alumno_seleccionar_proyecto, name='alumno_seleccionar_proyecto'),

    # empresa
    path('registro/empresa/', views.registro_empresa, name='registro_empresa'),
    path('empresa/home', views.empresa_home, name='empresa_home'),
    path('empresa/perfil', views.empresa_perfil, name='empresa_perfil'),
    path('empresa/crearProyecto', views.empresa_crear_proyecto, name='empresa_crear_proyecto'),
    path('empresa/proyectos', views.empresa_proyectos, name='empresa_proyectos'),

    # administrador
    path('administrador/home', views.administrador_home, name='administrador_home'),
    path('administrador/perfil', views.administrador_perfil, name='administrador_perfil'),


    path('administrador/alumnos/', views.administrador_alumnos, name='administrador_alumnos'),
    path('administrador/alumnos/editar/<int:alumno_id>/', views.editar_alumno, name='editar_alumno'),
    path('administrador/alumnos/eliminar/<int:alumno_id>/', views.eliminar_alumno, name='eliminar_alumno'),
    
    
    path('administrador/empresas/', views.administrador_empresas, name='administrador_empresas'),
    path('administrador/empresas/editar/<int:empresa_id>/', views.editar_empresa, name='editar_empresa'),
    path('administrador/empresas/eliminar/<int:empresa_id>/', views.eliminar_empresa, name='eliminar_empresa'),


    path('administrador/proyectos/', views.administrador_proyectos, name='administrador_proyectos'),
    path('administrador/proyectos/editar/<int:proyecto_id>/', views.editar_proyecto, name='editar_proyecto'),
    path('administrador/proyectos/eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),


    path('administrador/proyectos_seleccionados/', views.administrador_proyectos_seleccionados, name='administrador_proyectos_seleccionados'),
    path('administrador/proyectos_seleccionados/eliminar/<int:proyectoalumno_id>/', views.eliminar_proyecto_seleccionado, name='eliminar_proyecto_seleccionado'),


    path('administrador/alumnos/exportar', views.exportar_alumnos, name='exportar_alumnos'),
    path('administrador/empresas/exportar', views.exportar_empresas, name='exportar_empresas'),
    path('administrador/proyectos/exportar', views.exportar_proyectos, name='exportar_proyectos'),
    path('administrador/proyectos_seleccionados/exportar', views.exportar_proyectos_seleccionados, name='exportar_proyectos_seleccionados'),
]
