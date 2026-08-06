from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Invitation, Rsvp

@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('bride_name', 'groom_name', 'wedding_date')

@admin.register(Rsvp)
class RsvpAdmin(admin.ModelAdmin):
    list_display = ('name', 'attending', 'created_at')