from django.contrib import admin

from .models import Profile, SelectedStation, SelectedTransport



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(SelectedStation)
class StationAdmin(admin.ModelAdmin):
    pass


@admin.register(SelectedTransport)
class TransportAdmin(admin.ModelAdmin):
    pass
