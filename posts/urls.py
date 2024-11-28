from django.urls import path, include
from .views import *
urlpatterns = [
    path('add_post/', add_post, name="add_post"),
    path('edit/<int:id>', edit_post, name="edit_post"),
    path('delete/<int:id>', delete_post, name="del_post"),
]