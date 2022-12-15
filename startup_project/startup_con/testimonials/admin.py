from django.contrib import admin
from .models import Testimonial
# Register your models here.

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'avaiable')
    list_filter = ('name', 'profession', 'avaiable')
    search_fields = ('name', 'profession', 'avaiable')
    list_editable = ('profession', 'avaiable')