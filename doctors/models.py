# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class DoctorCred(models.Model):
	#DoctorID = models.AutoField(primary_key=False)

	DoctorUsername = models.CharField(max_length=50)
	DoctorPassword = models.CharField(max_length=50)

	def __str__(self):
		return self.DoctorUsername

class Medicines(models.Model):
	MedName = models.CharField(max_length=50)
	MedXLoc = models.IntegerField(default=0)
	MedYLoc = models.IntegerField(default=0)
	MedQuantity = models.IntegerField(default=0)

	def __str__(self):
		return self.MedName

class PatientCred(models.Model):
	#PatientID = models.AutoField(primary_key=True)

	PatientUsername = models.CharField(max_length=50)
	PatientPassword = models.CharField(max_length=50)

	AssignedDoctor = models.ForeignKey(DoctorCred, on_delete=models.CASCADE)

	def __str__(self):
		return self.PatientUsername
"""
class DoctorCredForm(forms.ModelForm):
	class: Meta:
		model = DoctorCred
		fields = ['DoctorPassword']
"""
