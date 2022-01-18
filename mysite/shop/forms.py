from .models import *
from django.db import models
from django.forms import ModelForm

class AddForm(ModelForm):
	class Meta:
		model = Inventory
		fields = ['date','item','qty','action','source_loc','source_buc','dest_loc','dest_buc']