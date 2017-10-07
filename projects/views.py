# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
import sendgrid
import os
from sendgrid.helpers.mail import *
from forms import *
from models import *
# Create your views here.

SENDGRID_API = settings.SENDGRID_API_KEY

def home_page(request):
    if request.method == 'POST':
            form = ContactForm(request.POST)
        # check whether it's valid:
            if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
                sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API)
                # grab form data
                contact_name = request.POST.get(
                'your_name'
                , '')
                contact_email = request.POST.get(
                    'email_address'
                , '')
                form_content = request.POST.get('message', '')
                # import ready for email
                from_email = Email(contact_email)
                to_email = Email("jamessandersoon@gmail.com")
                subject = contact_name
                content = Content("text/plain", form_content)
                mail = Mail(from_email, subject, to_email, content)
                response = sg.client.mail.send.post(request_body=mail.get())
                return redirect('home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})

def product_detail(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    project = get_object_or_404(Project_Info, pk=id)
    return render(request, "projectinfo.html", {'project': project})

def about_me(request):
        if request.method == 'POST':
                form = ContactForm(request.POST)
            # check whether it's valid:
                if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API)
                    # grab form data
                    contact_name = request.POST.get(
                    'your_name'
                    , '')
                    contact_email = request.POST.get(
                        'email_address'
                    , '')
                    form_content = request.POST.get('message', '')
                    # import ready for email
                    from_email = Email(contact_email)
                    to_email = Email("jamessandersoon@gmail.com")
                    subject = contact_name
                    content = Content("text/plain", form_content)
                    mail = Mail(from_email, subject, to_email, content)
                    response = sg.client.mail.send.post(request_body=mail.get())
                    return redirect('home')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = ContactForm()
        return render(request, "aboutme.html", {'form': form})
