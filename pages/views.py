from distutils.log import error
from django.views.generic import TemplateView , FormView, ListView
from .forms import ContactForm, SubscribedEmailForm, RequestQuoteForm
from .models import SubscribedEmail, Testimonial, Service
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.validators import validate_email




def home_page(request):
    testimonial = Testimonial.objects.all()
    # form  = SubscribedEmailForm()
    form  = SubscribedEmailForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            if SubscribedEmail.objects.filter(email=obj.email).exists() == False :
                send_mail(subject="Subscribe", message="thank you for subscribing {0}".format(obj.email), from_email="server@gmail.com",recipient_list=[obj.email])
                form.save()
                return JsonResponse({'message':"Thank you for subscribing"})
            else:
                return JsonResponse({'message':"This email already exists"})
        else:
            return JsonResponse({'message':"Enter a valid Email address"})


    return render(request, 'home.html', context={'testimonial':testimonial, 'formEmail':form})

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return JsonResponse({"valid": "Thank you for contacting us"})
    def form_invalid(self, form):
        return JsonResponse({"invalid": form.errors })

        # return super().form_valid(form)


class TestimonialView(ListView):
    model = Testimonial
    template_name = 'testimonial.html'


class ServiceView(ListView):
    model = Service
    template_name = 'service.html'
   
    

class AboutView(TemplateView):
    template_name = 'about.html'


class FeaturesView(TemplateView):
    template_name = 'features.html'


class TeamView(TemplateView):
    template_name = 'team.html'


class RequestQuoteView (FormView):
    template_name = 'quote.html'
    form_class  = RequestQuoteForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return JsonResponse({'valid':"Thank you for submitting"})
    
    def form_invalid(self, form):
        return JsonResponse({'invalid':form.errors})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)