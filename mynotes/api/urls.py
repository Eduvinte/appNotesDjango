from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/', views.getNote, name="notes"),
    path('notesDetails/<str:pk>/', views.getNoteDetail, name="note"),
] 

