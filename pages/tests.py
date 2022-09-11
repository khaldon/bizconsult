from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
from .models import Contact

class ContactTestForm(TestCase):
    def test_contact_page_found_or_not(self):
        response =  self.client.get('/contact/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_contact_view_name(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'contact.html')
    
    def test_contact_form(self):
        response = self.client.post(reverse('contact'), data={
            'name':"Hello world",
            "email":"mohamed.khaled33@gmail.com",
            "subject":"this is my object",
            "message":"Hello world in this is message"
        })
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Contact.objects.all().count(), 1)

