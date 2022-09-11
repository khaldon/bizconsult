from django.forms import ModelForm
from .models import Contact, SubscribedEmail


class ContactForm(ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'id':'name', 'placeholder':'Your Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'id':'email', 'placeholder':'Your Email'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control', 'id':'subject', 'placeholder':'Subject'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'id':'message', 'style':'height:150px', 'placeholder':'Leave a messsage here'})

    class Meta:
        model = Contact
        fields = '__all__'


class SubscribedEmailForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class':'form-control border-0 rounded-pill w-100 ps-4 pe-5',
            'style':'height: 48px'
            })

    class Meta:
        model = SubscribedEmail
        fields = "__all__"