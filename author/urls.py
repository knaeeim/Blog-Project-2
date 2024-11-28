from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('profile_dashboard/', profile, name="profile"),
    path('logout/', user_logout, name="logout"),
    path('update/', change_user_data, name="update"),
    path('update_password/', update_password, name="password"),
]
