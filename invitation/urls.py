from django.urls import path
from . import views

urlpatterns = [
    path('', views.invitation_view, name='invitation'),
]