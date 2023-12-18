from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):   # UserCreationForm 상속; 원래 username, password1, password2 속성을 가지고 있음;
    email = forms.EmailField(label='이메일')  # 이메일 속성 추가
    class Meta:
        model = User
        fields = {"username", "password1", "password2", "email"}