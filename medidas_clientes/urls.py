
from django.contrib import admin
from django.urls import path
from app_medidas_clientes import views
from app_medidas_clientes.views import buscar_pessoas, cadastrar_pessoa

urlpatterns = [
    #rota, view responsável, nome de referência
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('buscar/', buscar_pessoas, name='buscar_pessoas'),
    path('cadastrar-pessoa/', cadastrar_pessoa, name='cadastro-pessoa'),
    path('pessoa/<int:pessoa_id>/', views.exibir_pessoa, name='detalhes_pessoa'),
    path('todas-pessoas/', views.todas_pessoas, name='todas_pessoas'),
]