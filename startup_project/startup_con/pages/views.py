from django.shortcuts import render
from django.views.generic import TemplateView, ListView 
from django.views.generic.edit import FormView
from testimonials.models import Testimonial
from team.models import Team, SocMedia
from blogs.models import Blog
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.all()
        context['teams'] = Team.objects.all()
        context['socmedia'] = SocMedia.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

def service(request):
    return render(request, 'service.html')

class ContactView(SuccessMessageMixin,FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'Your message has been sent successfully'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


    