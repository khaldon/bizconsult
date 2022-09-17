from ast import Sub
from django.contrib import admin
from .models import Contact, SubscribedEmail, Testimonial, RequestQuote, Service
# Register your models here.

admin.site.register(Contact)
admin.site.register(SubscribedEmail)
admin.site.register(Testimonial)
admin.site.register(RequestQuote)
admin.site.register(Service)