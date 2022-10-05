from django.urls import path, re_path
from . import views

# lista con metodo path importado de libreria django modulo urls:
# primer parametro ruta,
# segundo parametro metodo de views debe asociar a esta ruta,
urlpatterns = [
    path('hola_mundo', views.hola_mundo),
    path('saludar/', views.saludar, name='saludar_solito'),
    # url parametrizada
    path('saludar/<str:nombre>', views.saludar, name='saludar'),
    # rutas de proyectos
    # name="ver_proyectos" alias completa la ruta para usarlo en templates o redirecciones a ruta especifica (evita hardcodear rutas)
    path('proyectos/<int:anio>/<int:mes>/',
         views.ver_proyectos, name="ver_proyectos"),
]
