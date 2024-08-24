from django.shortcuts import render, redirect

from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('success', first_name=contact.first_name)
    else:
        form = ContactForm()
    return render(request, 'contactForm/index.html', {
        'form' : form
    })

def success_view(request, first_name):
    return render(request, 'contactForm/success.html', {
        'first_name': first_name
    })