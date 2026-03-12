from django.shortcuts import render, get_object_or_404
from .models import Language

def home(request):
    # Получаем все языки из базы, отсортированные по полю order
    languages = Language.objects.all()
    # Передаём в шаблон
    return render(request, 'languages/home.html', {'languages': languages})

def language_detail(request, lang_slug):
    # Получаем один язык по слагу или выдаём 404
    language = get_object_or_404(Language, slug=lang_slug)
    return render(request, 'languages/language_detail.html', {'language': language})
