# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def index(request):
    context = {
                    'test': True,
                }

    return render(request, 'signup/index.html', context)
