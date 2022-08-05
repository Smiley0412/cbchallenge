from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.messages_list),
    path('messages/<int:pk>/', views.message_detail),
    path('users/', views.user_list)
]