from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('all', views.UserCharactersView.as_view(), name='all-characters'),
    path('create/', views.AddCharacterView.as_view(), name='add-character'),
    path('update/<int:pk>/', views.UpdateCharacterView.as_view(),
         name='update-character'),
    path('delete/<int:pk>/', views.DestroyCharacterView.as_view(),
         name='delete-character')]
