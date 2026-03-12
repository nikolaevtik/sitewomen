from django import forms

from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.utils.deconstruct import deconstructible
from .models import Category, Husband, Women


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮ0Я1234567890- "
    code = "russian"

    def __init__(self, message=None):
        self.message = (
            message
            if message
            else "Должны присутствовать тооько русские буквы, дефис и пробел"
        )

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise forms.ValidationError(self.message, code=self.code)


class AddPostForm(forms.ModelForm):

    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Категория не выбрана",
        label="Категории",
    )
    husband = forms.ModelChoiceField(
        queryset=Husband.objects.all(),
        empty_label="Не замужем",
        required=False,
        label="Муж",
    )

    class Meta:
        model = Women
        fields = ['title','slug','content','photo','is_published','cat','husband','tags']
        widgets={'title':forms.TextInput(attrs={'class': ' form-input'}),
                 'content': forms.Textarea(attrs ={'cols': 50, 'rows':5})}
        
        labels = {'slug': ' URL'}
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise forms.ValidationError("Длина превышает 50 символов")
        return title
    
    
    
class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')