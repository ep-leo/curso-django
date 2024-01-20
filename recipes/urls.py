from django.urls import path
from recipes.views import sobre

urlpatterns = [
    path('sobre/', sobre)
]