from django.urls import path
from .views import manager_page

app_name = 'manager'

urlpatterns = [
    path('', manager_page, name='manager_page'),
]