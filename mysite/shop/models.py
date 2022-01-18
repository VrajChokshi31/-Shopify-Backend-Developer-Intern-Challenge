from django.db import models
from django_better_choices import Choices

# Create your models here.
class ACTION_CHOICES(Choices) :
	SHIPPING = 'Shipping'
	RECEIVING = 'Receiving'
	SALE_ITEM = 'Sale Item'
	TRANSFER_ITEM = 'Transfer Item'


class BUC(Choices) :
	DEFAULT = ' '
	ON_HAND = 'On Hand'
	AT_VENDOR = 'At Vendor'
	SHIPPED = 'Shipped'
	SOLD = 'Sold'
	PRE_SALE = 'Pre-Sale'

class LOC(Choices) :
	DEFAULT = 'Default'

class Inventory(models.Model) :
	date = models.DateTimeField()
	item = models.IntegerField()
	qty = models.FloatField(default=0)
	action = models.CharField(max_length = 100, choices = ACTION_CHOICES, default = ACTION_CHOICES.SALE_ITEM)
	source_loc = models.CharField(max_length = 100, choices = LOC, default = LOC.DEFAULT) 
	source_buc = models.CharField(max_length = 100, choices = BUC, default = BUC.DEFAULT)
	dest_loc = models.CharField(max_length = 100, choices = LOC, default = LOC.DEFAULT)  
	dest_buc = models.CharField(max_length = 100, choices = BUC, default = BUC.DEFAULT)