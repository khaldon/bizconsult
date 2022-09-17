import email
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject  = models.CharField(max_length=290)
    message = models.TextField()

    def __str__(self):
        return self.subject 


class SubscribedEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=50)
    client_image = models.ImageField(upload_to='images')
    text = models.TextField()

    def __str__(self):
        return self.client_name

    

class RequestQuote(models.Model):
    CHOICES = [
        ('financial','Financial Consultancy'),
        ('strategy','Strategy Consultancy'),
        ('tax','Tax Consultancy')]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=9,choices=CHOICES, default='financial')
    comment = models.TextField()

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=190)
    content = models.TextField()

    def __str__(self):
        return self.title

