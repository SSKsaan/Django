from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from . import forms

# Create your views here.
def Home(request):
    if request.method == 'POST':
        form = forms.Email_Form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            send_email(email, subject, content, 'mail.html')
            return render(request, 'index.html', {'form': form})
    else:
        form = forms.Email_Form()
    return render(request, 'index.html', {'form': form})
    

def send_email(email, subject, content, template):
        message = render_to_string(template, {
            'email': email,
            'subject': subject,
            'content': content,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()