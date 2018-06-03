# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

""" 
Admin credentials:
	Username: admin
	Password: sihamd123
"""

from .models import DoctorCred,PatientCred,Medicines

admin.site.register(DoctorCred)
admin.site.register(PatientCred)
admin.site.register(Medicines)