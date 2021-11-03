from django.forms import ModelForm, widgets
from django.forms import fields
from news.models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Order
class Orderfrom(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreatUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class CommentForm(forms.Modelforms):
    content = forms.CharField(widget=forms.Textarea(attrs={
            'rows':'4',
    }))
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content' )
        