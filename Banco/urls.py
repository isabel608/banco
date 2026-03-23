"""
URL configuration for Banco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro_clientes/', registrar_cliente, name='registrar_clientes'),
    path('registro_cuentas/', registrar_cuenta, name='registrar_cuentas'),
    path('registro_transaccion/', registrar_transaccion, name='registrar_transaccion'),
    path('consultas/',consultas,name='consultas'),
    path('registro/',registro,name='registro'),
    path('visualizar/int:<cliente_dpi>',visualizar,name='visualizar'),
    path('transferencia/int:<numero_cuenta>',transferencia,name='transferencia'),
    path('guardartransa/int:<numero_cuenta>',guardartransa,name='guardartransa'),
]
