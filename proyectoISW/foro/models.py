from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(default='Hola, soy nuevo usuario!', max_length=100)
    image = models.ImageField(default='C:\\Users\\J Suarez\\Documents\\PROYECTO_ISW\\proyectoISW\\foro\\static\\img\\new_user.png')
    
    def __str__(self) -> str:
        return f'Perfil de {self.user.username}'

class Tema_post(models.Model):
    descrip = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.descrip

class Post(models.Model):

    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='posts')
    likes = models.IntegerField(default=0)
    user_likes = models.ManyToManyField(User, blank=True)
    tema = models.ForeignKey(Tema_post, on_delete = models.CASCADE, related_name='posts', default=1)
    ofensivo = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def comentarios(self):
        return Comment.objects.filter(post = self)
    
    def __str__(self) -> str:
        return self.content

class Comment(models.Model):

    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='comments')
    likes = models.IntegerField(default=0)
    user_likes = models.ManyToManyField(User, blank=True)
    ofensivo = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

