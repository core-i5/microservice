from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    # User
    path('user/create-user/', CreateUserView.as_view(), name='create-user'),
    path('user/get-user-list/', GetUserListView.as_view(), name='get-user-list'),
    path('user/get-user/<int:pk>/', GetUserView.as_view(), name='get-user'),
    path('user/delete-user/<int:pk>/', DeleteUserView.as_view(), name='delete-user'),
    path('user/update-user/<int:pk>/', UpdateUserView.as_view(), name='update-user'),
]