# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Cities
from .forms import SignupForm
from django.views.generic import FormView
from django.http import HttpResponse


def index(request):

    cities = [c.city + ', ' + c.state
                for c in Cities.objects.order_by('city')]

    context = {
                    'cities': cities,
                }

    return render(request, 'signup/index.html', context)


class SignupFormPage(FormView):
    template_name = 'signup/index.html'
    success_url = '/awesome/'
    form_class = SignupForm

    def form_valid(self, form):
            return HttpResponse("Sweeeeeet.")
