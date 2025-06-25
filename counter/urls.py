from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),       # maps base URL to home view
    path('count/', views.count, name='count'),
]
