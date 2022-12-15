from django.shortcuts import render
from .models import Testimonial
# Create your views here.

def testimonials(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials
    }
    return render(request, 'testimonials.html', context)