from django.contrib import admin

# Register your models here.
from .forms import ProfileForm
from .models import Profile
from .models import Message
from .models import SelectedStation
from .models import SelectedTransport


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name')
    form = ProfileForm
    search_fields = ['external_id']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_at')

    # def get_queryset(self, request):
    #     return


@admin.register(SelectedStation)
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'station', 'created_at')


@admin.register(SelectedTransport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'transport', 'created_at')
