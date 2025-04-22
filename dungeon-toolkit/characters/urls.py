from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('chars', views.UserCharactersView.as_view(), name='characters'),
    path('create/', views.add_character, name='add-character'),
    #path('all/', views.view_items, name='view_items'),
    path('update/<int:pk>/', views.update_character, name='update-character'),
    path('item/<int:pk>/delete/', views.delete_character, name='delete-character'),
]
