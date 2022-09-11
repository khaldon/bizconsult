from django.views.generic import TemplateView , FormView, ListView
from .forms import ContactForm, SubscribedEmailForm
from .models import SubscribedEmail, Testimonial
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.shortcuts import render,get_object_or_404


class HomePageView(TemplateView, FormView):
    template_name = 'home.html'
    form_class = SubscribedEmailForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        send_mail(subject="Subscribe", message="thank you for subscribing {0}".format(obj.email), from_email="server@gmail.com",recipient_list=[obj.email])
        if SubscribedEmail.objects.filter(email=obj.email).exists() == False :
            obj.save()
            return super().form_valid(form)
        else:
            return super().form_valid(form)



class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# class SubscribedEmailView(FormView):
#     template_name = 'newsletter.html'
#     form_class = SubscribedEmailForm
#     success_url = reverse_lazy('home')
    
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         send_mail(subject="Subscribe", message="thank you for subscribing {0}".format(obj.email), from_email="server@gmail.com",recipient_list=[obj.email])
#         if SubscribedEmail.objects.filter(email=obj.email).exists() == False :
#             obj.save()
#             return super().form_valid(form)
#         else:
#             return super().form_valid(form)


class TestimonialView(ListView):
    model = Testimonial
    template_name = 'testimonial.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ServiceView(TemplateView):
    template_name = 'service.html'

class FeaturesView(TemplateView):
    template_name = 'features.html'


class TeamView(TemplateView):
    template_name = 'team.html'


class QuoteView(TemplateView):
    template_name = 'quote.html'

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)