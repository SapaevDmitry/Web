"""
Definition of forms.
"""
from django.db import models
from.models import Comment
from.models import Blog

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Ваш пол',
                             choices=[('1', 'Да'), ('2', 'Нет')],
                             widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label='Вы пользуетесь интернетом',
                             choices=(('1','Не пользовался услугами'),
                                      ('2','Один раз'),
                                      ('3','До пяти раз'),
                                      ('4','Более 5 раз')), initial=1)
    notice = forms.BooleanField(label='Получать новости сайта на почту?',
                                required=False)
    email = forms.EmailField(label='Ваша почта', min_length=7)
    message = forms.CharField(label='Пожелания по работе нашей компании',
                              widget=forms.Textarea(attrs={'rows':12,'cols':20}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text':"Комментарий"}


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}
