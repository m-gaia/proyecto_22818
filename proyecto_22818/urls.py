"""proyecto_22818 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# administrar rutas
# rutas disponibles y con que metodos de la capa vista se va a asociar
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    # esta ruta tiene un prefijo admin
    path('admin/', admin.site.urls),
    # asociar urls.py del proyecto a urls.py de las app para renderizar ej http://127.0.0.1:8000/hola_mundo
    # http://127.0.0.1:8000/saludar/Maru
    path('', include('cac.urls'))

]
