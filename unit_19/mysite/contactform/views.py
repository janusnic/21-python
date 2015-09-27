from django.shortcuts import render

from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('name', ''):
            errors.append('Enter your name.')
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
          try:
            send_mail(
                request.POST['name'],
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'support@ruunalbe.com'),
                ['siteowner@example.com'],
            )
            return HttpResponse('Thank you, form has been submitted successfully')
          except Exception, err: 
            return HttpResponse(str(err))
    return render(request, 'contactform/contact_form.html',{'errors': errors})

def contact1(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render(request, 'contact_form.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })