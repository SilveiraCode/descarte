from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),  

    path('solicitar/', views.nova_solicitacao, name='nova_solicitacao'),

    path('solicitacoes/', views.lista_solicitacoes, name='lista_solicitacoes'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('cadastro/', views.cadastro, name='cadastro'),

    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)