from django.urls import path
from oapp.views import index

urlpatterns = [
    path('', index, name='index'),
]