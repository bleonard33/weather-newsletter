# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import SignupForm


def index(request):

    context = {
                'form': SignupForm,
                'message': None
              }

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            context['message'] = 'Success! Thanks for signing up.'
            print form.cleaned_data

    return render(request, 'signup/index.html', context)
