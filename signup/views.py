# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import os


def index(request):
    context = {
                    'api_key': os.environ['WUNDERGROUND_KEY'],
                }

    return render(request, 'signup/index.html', context)
