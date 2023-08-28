from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError 
 
class CustomUserCreationForm(UserCreationForm): 
    username = forms.CharField(label='Никнейм пользователя', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}) , min_length=5, max_length=150)
    email = forms.EmailField(label='Электронная почта', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})) 
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})) 
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))  

    def clean_password2(self): 
        password1 = self.cleaned_data['password1'] 
        password2 = self.cleaned_data['password2'] 
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароль не совпадает")  
        return password2

    def save(self, commit = True): 
        user = User.objects.create_user( 
            self.cleaned_data['username'], 
            self.cleaned_data['email'], 
            self.cleaned_data['password1'] 
        ) 
        return user 
