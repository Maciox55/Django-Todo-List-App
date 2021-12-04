from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.create_todo, name="create_todo"),
    path('delete/<int:id>',views.delete, name="delete"),
    path('delete/<int:id>/', views.delete_todo, name="delete-task"),
    path('complete/<int:id>',views.complete_todo,name="complete_todo"),
    path('update/<int:id>',views.update,name="update"),
]