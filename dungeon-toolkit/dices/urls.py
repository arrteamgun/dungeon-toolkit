from django.urls import path
from .views import DicesView

app_name = 'dices'

urlpatterns = [
    path('', DicesView.as_view(), name='dices'),
]
