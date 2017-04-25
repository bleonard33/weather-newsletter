# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Cities(models.Model):
    city = models.CharField(max_length=48)
    state = models.CharField(max_length=2)

    def __str__(self):
        return '{c}, {s}'.format(c=self.city, s=self.state)


class Account(models.Model):
    email_address = models.EmailField()
    location = models.ForeignKey(Cities)
