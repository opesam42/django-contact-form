from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    agree_terms = forms.BooleanField(
        label="I consent to being contacted by the team.",  # Custom label text
        required=True,  # Make it a required field
        error_messages={
            'required': 'Please confirm that you agree to be contacted by the team.'
        }
    ) 
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'query_method', 'message', 'agree_terms']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'First Name'}),
            'last_name': forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter your email'}),
            'query_method' : forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
        }
        error_messages = {
            'first_name': {
                'required': 'Please enter your first name.',
            },
            'last_name': {
                'required': 'Please enter your last name.',
            },
            'email': {
                'required': 'Please enter your email.',
            },
            'query_method': {
                'required': 'Please select a query type.',
            },
        }
