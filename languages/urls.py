from django.urls import path
from . import views

app_name = 'languages'  # <-- добавить

urlpatterns = [
    path('', views.home, name='home'),           # /lang/
    path('<slug:lang_slug>/', views.language_detail, name='language_detail'),  # /lang/python/
]