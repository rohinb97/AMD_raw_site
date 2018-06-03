# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Medicines,DoctorCred,PatientCred
from django.shortcuts import render
from django.views import generic

# Create your views here.

def login(request):
	
	return render(request,'doctors/login.html')

def accountPage(request,DoctorUsername):
	output = ""
	output = output + "Welcome %s !" % DoctorUsername
	return HttpResponse(output)

def prescription(request):
	medicine = Medicines.objects.order_by('id')
	return render(request,'doctors/prescription.html',{
		'medicines':medicine
		})

def getQRCode(request):
	if request.method == 'POST':
		med = Medicines.objects.filter(MedName__startswith=request.get())
		response = dict()
		for i,m in enumerate(med):
			response.update({i:{
			'MedName':m.MedName,
			'MedXLoc':m.MedXLoc,
			'MedYLoc':m.MedYLoc,
			'MedQuantity':m.MedQuantity
			}})
		r = JsonResponse(response)
	else:
		return HttpResponse("Looks like a bad request")

def patientHistory(request,id,AssignedDoctor_id):
	output = ""
	output = output + "View patient history here."
	return HttpResponse(output)
