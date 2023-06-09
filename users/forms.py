from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from .models import Commentaire, Personnell, Projett, Service,Contact



class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'First Name','class': 'form-control', }))
    last_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'Last Name','class': 'form-control',}))
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control',}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email','class': 'form-control', }))
    password1 = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control','data-toggle': 'password','id': 'password',}))
    password2 = forms.CharField(max_length=50, required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class': 'form-control','data-toggle': 'password','id': 'password',}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control',}))
    password = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control','data-toggle': 'password','id': 'password','name': 'password',}))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']





class ServiceForm(ModelForm):
    class Meta :
        model = Service
        fields = "__all__" 
        
class ProjetForm(ModelForm):
    class Meta :
        model = Projett
        fields = "__all__" 
        
class PersonnelForm(ModelForm):
    class Meta :
        model = Personnell
        fields = "__all__" 
        
class ContactForm(ModelForm):
    class Meta :
        model = Contact
        fields = "__all__" 
        
class CommentaireForm(ModelForm):
    class Meta :
        model = Commentaire
        fields =  ["content"]