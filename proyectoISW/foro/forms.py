from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile, Comment
 
	
class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form3Example2c'})) 
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form3Example2c'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'form3Example3c'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form3Example4c'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form3Example4c'}))
	
	class Meta:
		model = User
		fields = ['first_name', 'username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control w-100',
								'id':'contentsBox', 'rows':'5',
								'placeholder':'Consulta sin límite!'}))

	class Meta:
		model = Post
		fields = ['content']

class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={ 'class': "form-control w-100",
								'id':'contentsBox', 'rows':'2',
								'placeholder':'¿Tienes alguna opinión?'}))

	class Meta:
		model = Comment
		fields = ['content']