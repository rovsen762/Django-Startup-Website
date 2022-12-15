from django.contrib import admin
from .models import Team, SocMedia

# Register your models here.


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'avaiable')
    list_filter = ('name', 'position', 'avaiable')
    search_fields = ('name', 'position', 'avaiable')
    list_editable = ('position', 'avaiable')

@admin.register(SocMedia)
class SocMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'team')
    list_filter = ('name', 'link', 'team')
    search_fields = ('name', 'link', 'team')
    list_editable = ('link', 'team')

