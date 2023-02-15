from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    # User
    path('user/get-user-list/', GetUserListView.as_view(), name='get-user-list'),
    path('user/update-user-infection-probability/<int:pk>/', UpdateUserView.as_view(), name='update-user'),

]