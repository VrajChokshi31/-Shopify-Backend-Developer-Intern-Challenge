from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib import messages
import csv


def index(request):
    return render(request, 'shop/Main.html')

def ViewItem(request):
	inventory = Inventory.objects.all()
	return render(request,'shop/View-Item.html', {'inventory':inventory})

def ModifyItem(request):
	return render(request,'shop/Modify-Item.html')

def AddItem(request):
	return render(request,'shop/Add-Item.html')

def DeleteItem(request):
	return render(request,'shop/Delete-Item.html')

def Export(request):
	return render(request,'shop/Export.html')

def add(request):
	try:
		f = Inventory(action=request.POST['action'], date=request.POST['date'], item=request.POST['item'], source_loc=request.POST['source_loc'], dest_loc=request.POST['dest_loc'], source_buc=request.POST['source_buc'], dest_buc=request.POST['dest_buc'], qty=request.POST['qty'])
	except :
		return render(request,'shop/Add-Item.html')
	else :
		f.save()
		return render(request,'shop/Add-Item.html')

def mod(request):
	try:
		a = Inventory.objects.get(id=request.POST['serial'])
		a.action=request.POST['action']
		a.date=request.POST['date']
		a.item=request.POST['item']
		a.source_loc=request.POST['source_loc']
		a.dest_loc=request.POST['dest_loc']
		a.source_buc=request.POST['source_buc']
		a.dest_buc=request.POST['dest_buc']
		a.qty=request.POST['qty']
	except :
		return render(request,'shop/Modify-Item.html')
	else :
		a.save()
		return render(request,'shop/Modify-Item.html')

def delete(request):
	try:
		f = Inventory.objects.get(id=request.POST['serial'])
	except :
		return render(request,'shop/Delete-Item.html')
	else :
		f.delete()
		return render(request,'shop/Delete-Item.html')

def download_csv(request, queryset):
 
  #if not request.user.is_staff:
   #raise PermissionDenied

  model = queryset.model
  model_fields = model._meta.fields + model._meta.many_to_many
  field_names = [field.name for field in model_fields]

  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="export.csv"'

  # the csv writer
  writer = csv.writer(response, delimiter=",")
  # Write a first row with header information
  writer.writerow(field_names)
  # Write data rows
  for row in queryset:
      values = []
      for field in field_names:
          value = getattr(row, field)
          if callable(value):
              try:
                  value = value() or ''
              except:
                  value = 'Error retrieving value'
          if value is None:
              value = ''
          values.append(value)
      writer.writerow(values)
  return response

def myview(request):
  # Create the HttpResponse object with the appropriate CSV header.
  data = download_csv(request, Inventory.objects.all())
  response = HttpResponse(data, content_type='text/csv')
  return response
