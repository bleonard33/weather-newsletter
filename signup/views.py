# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib import messages
from .models import Account
from .forms import SignupForm


def index(request):
    if request.method == 'POST':
        # POST on form submission
        form = SignupForm(request.POST)

        # Validate django form
        if form.is_valid():

            # Select account rows where email is the one entered
            query = Account.objects.filter(
                email_address=form.cleaned_data['email_address'])

            # If no record for that email, save and report success
            if not query.exists():
                form.save()
                messages.success(request, 'Success! Thanks for signing up.')

            # If record exists, send failure message
            else:
                messages.error(request, 'Email address already registered.')

        # Invalid form data
        else:
            messages.error(request, 'Something went wrong!')

    return render(request, 'signup/index.html', {'form': SignupForm})
