from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from foro import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', LoginView.as_view(template_name='foro/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', views.Home, name='Home'),
    path('perfil/', views.Perfil, name='Perfil'),
    path('registro/', views.Registro, name='Registro'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('likes/<int:post_id>/', views.likes, name='likes'),
    path('likes_comment/<int:comment_id>/', views.likes_comment, name='likes_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
