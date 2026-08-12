from django.urls import path
from . import views

urlpatterns = [
    path('', views.invitation_view, name='invitation'),
    path('rsvp/<int:invitation_id>/', views.rsvp_submit, name='rsvp_submit'),
]