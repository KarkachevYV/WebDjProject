from .models import Reviews_post
from django.forms import ModelForm, TextInput, Textarea

class Reviews_postForm(ModelForm):
    class Meta:
        model = Reviews_post
        fields = ['title', 'description', 'movie_review', 'author']
        widgets = {
            'title': TextInput(attrs={'class':'form-control', 'placeholder':'Введите название фильма'}),
            'description': TextInput(attrs={'class':'form-control', 'placeholder':'Введите краткое описание'}),
            'movie_review': Textarea(attrs={'class':'form-control', 'placeholder':'Введите свой отзыв'}),
            'author': TextInput(attrs={'class':'form-control', 'placeholder':'Укажите свои ФИО'}),
        }