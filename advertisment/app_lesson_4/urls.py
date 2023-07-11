from django.urls import path
from .views import index_app_l4

urlpatterns = [
    path('lesson_4', index_app_l4)
]