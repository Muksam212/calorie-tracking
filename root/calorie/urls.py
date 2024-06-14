from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("calorie/<int:id>/", views.delete_consume, name = "delete-consume")
]
