from django.urls import path
from .views import index_app_l4

urlpatterns = [
    path('', index_app_l4)
]
