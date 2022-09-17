from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import (handler400, handler403, handler404, handler500)
handler404 = 'pages.views.page_not_found_view'

urlpatterns = [
        path('', views.home_page, name='home'),
        path('testimonial', views.TestimonialView.as_view(), name='testimonial'),
        path('contact/', views.ContactView.as_view(), name="contact"),
        path("about/", views.AboutView.as_view(), name='about'),
        path("service/", views.ServiceView.as_view(), name='service'),
        path("features/", views.FeaturesView.as_view(), name='features'),
        path("team/", views.TeamView.as_view(), name='team'),
        path("quote/", views.RequestQuoteView.as_view(), name='quote'),

]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


