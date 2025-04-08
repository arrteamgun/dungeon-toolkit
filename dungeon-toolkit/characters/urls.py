from django.urls import path
from .views import UserCharactersView

app_name = 'characters'

urlpatterns = [
    #path('<slug:char_slug>', UserCharactersView.as_view(), name='characters'),
    path('chars', UserCharactersView.as_view(), name='characters'),
]
