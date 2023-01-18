from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Comment, Tema_post
from .forms import UserRegisterForm, PostForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth import login
from datetime import datetime
from django.contrib import messages
import joblib


def clasificaa(texto):
    tfidf = joblib.load('C:\\Users\\J Suarez\\Documents\\PROYECTO_ISW\\proyectoISW\\foro\\tfidf.pkl')
    model = joblib.load('C:\\Users\\J Suarez\\Documents\\PROYECTO_ISW\\proyectoISW\\foro\\model.pkl')
    test = tfidf.transform([texto]).toarray()
    return model.predict(test)[0]

@login_required
def Home(request):

    # blog
    posts = Post.objects.all()
    temas = Tema_post.objects.all()
    form = PostForm()
    form2 = CommentForm()
    if request.method == 'POST':
        if request.POST.get('form_type') == "post":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.tema = Tema_post.objects.get(descrip=request.POST.get('tema'))
                if clasificaa(post.content) == 1:
                    post.ofensivo = True
                post.save()
                HttpResponseRedirect(reverse('Home'))
        elif request.POST.get('form_type') == "comment":
            form = CommentForm(request.POST)
            print("dentro")
            if form.is_valid():
                print("valido")
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = Post.objects.get(id=request.POST.get('post_id'))
                if clasificaa(comment.content) == 1:
                    comment.ofensivo = True
                comment.save()
                return HttpResponseRedirect(reverse('Home'))
    
    context = {'posts':posts, 'form' : form, 'form2' : form2, 'temas':temas}
    return render(request, "foro/home.html", context)

@login_required
def Perfil(request):

    # ver perfil de usuario, publicaciones y datos
    return render(request, "foro/perfil.html")

def Registro(request):
    
    if request.method == 'POST':
        print("dentro")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            form.save()
            messages.success(request, 'Te registraste con éxito.')
            login(request, user)
            return redirect('Home')
    else:
        form = UserRegisterForm()
        
    context = {'form' : form}
    return render(request, 'foro/registro.html', context)

def delete(request, post_id):
    post = Post.objects.get(id=post_id) 
    post.delete()
    messages.success(request,  'Publicación eliminada con éxito.')
    return HttpResponseRedirect(reverse('Home'))

def likes(request, post_id):
    post = Post.objects.get(id=post_id)
    post.likes = post.likes + 1
    post.save()
    return HttpResponseRedirect(reverse('Home'))

def likes_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.likes = comment.likes + 1
    comment.save()
    return HttpResponseRedirect(reverse('Home'))

def post_likes_user(request, post_id, user_id):

    try: 
        post_user = post_likes_user.objects.get(post_like = post_id, user_likes = user_id)  
    except:
        print("no encontrado")