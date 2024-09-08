from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask, name='addTask'),
    path('done/<int:pk>/', views.done, name='done'),
    path('undone/<int:pk>/', views.undone, name='undone'),
    path('editTask/<int:pk>/', views.editTask, name='editTask'),
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
]
