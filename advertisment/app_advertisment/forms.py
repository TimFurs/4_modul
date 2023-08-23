from django import forms
from django.core.exceptions import ValidationError

from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title','description','price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
        }

    def clean_title(self):
        if title.startswith('?'):
            raise ValidationError('Заголовок не может')





    #title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), label='Заголовок')
    #description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}), label='Описание')
    #price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),min_value=0, label='Цена')
    #auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False,label='Возможность торга')
    #image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}), label='Изображение', required=False)
