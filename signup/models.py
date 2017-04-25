# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Account(models.Model):
    email_address = models.EmailField()
    location = models.CharField(max_length=50)
