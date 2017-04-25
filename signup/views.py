# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Cities
from .forms import SignupForm
from django.views.generic import FormView
from django.http import HttpResponse


def index(request):

    if request.method == 'POST':
        print request

    context = {
                'form': SignupForm
              }

    return render(request, 'signup/index.html', context)
