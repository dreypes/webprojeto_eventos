"""
URL configuration for eventos_projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
from django.urls import path
from app_eventos import views
#from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    
    # Caminho para o sistema de gestão de eventos
    path('gestao_eventos/', views.gestao_eventos, name='gestao_eventos'),
    
    # Usuário
    path('usuarios/criar/', views.criar_usuario, name='criar_usuario'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),

    # Locais
    path('local/novo', (views.criar_local), name='criar_local'),
    path('local/alterar/<int:id>/', (views.criar_local), name='editar_local'),
    path('local/excluir/<int:id>/', (views.excluir_local), name='excluir_local'),
    path('locais/', (views.listar_locais), name='listar_locais'),

    # Eventos
    path('evento/novo', (views.criar_evento), name='criar_evento'),
    path('evento/alterar/<int:id>/', (views.criar_evento), name='editar_evento'),
    #path('evento/excluir/<int:id>/', (views.excluir_evento), name='excluir_evento'),
    path('eventos/', (views.listar_eventos), name='listar_eventos'),

    # Convites
    path('convites/criar/', views.criar_convite, name='criar_convite'),
    path('convite/enviar/<int:evento_id>/', (views.enviar_convite), name='enviar_convite'),
    path('convite/gerenciar/<int:convite_id>/', (views.gerenciar_convite), name='gerenciar_convite'),

    # Visualização de eventos para convidados
    path('eventos/convidado/', (views.listar_eventos_convidado), name='listar_eventos_convidado'),
    path('evento/<int:evento_id>/', (views.visualizar_evento), name='visualizar_evento'),
]
