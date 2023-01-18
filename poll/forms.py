from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question,Choice
from django.forms import ModelForm

#REGISTRATION FORM
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","phone_number",'password1','password2']



#POST FORM
class PostQuestion(ModelForm):
    class Meta:
        model = Question
        fields = ["question"]

class PostChoises(ModelForm):
    class Meta:
        model = Choice
        fields = ["question","option"]
