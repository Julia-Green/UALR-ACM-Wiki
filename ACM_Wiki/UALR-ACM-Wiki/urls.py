from django.urls import path
from ACM_Wiki.views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
