from django.db import models

# Create your models here.
class Contact(models.Model):
    QUERY_METHOD_CHOICES = [
        ('gen_enq', 'General Enquiry'),
        ('support', 'Support Request'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    query_method = models.CharField(max_length=30, choices=QUERY_METHOD_CHOICES, blank=False, null=False)
    message = models.TextField()
    agree_terms = models.BooleanField(default=False)