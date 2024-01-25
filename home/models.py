from django.db import models
from django.urls import reverse
from django.forms import modelformset_factory
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class ContactMessage (models.Model):
	uname = models.CharField(default='',max_length=40,null=True)
	age = models.IntegerField(default='')
	bmi = models.IntegerField(default='')
	wtoh = models.IntegerField(default='')
	ht = models.IntegerField(default='')
	pardimen = models.IntegerField(default='')
	fpg = models.IntegerField(default='')
	date = models.DateTimeField(auto_now_add=True)
	result = models.IntegerField(default='0',null=True)

class DmAlert(models.Model):
	uname = models.CharField(max_length=40,null=True)
	urine = models.IntegerField(default='')
	tried = models.IntegerField(default='')
	eat = models.IntegerField(default='')
	wound = models.IntegerField(default='')
	eye = models.IntegerField(default='')
	dehy = models.IntegerField(default='')
	hungry = models.IntegerField(default='')
	pain = models.IntegerField(default='')
	date = models.DateTimeField(auto_now_add=True)
	alertresult = models.IntegerField(default='0',null=True)

class DmBefore(models.Model):
	uname = models.CharField(max_length=40,null=True)
	bq1 = models.IntegerField(default='')
	bq2 = models.IntegerField(default='')
	bq3 = models.IntegerField(default='')
	bq4 = models.IntegerField(default='')
	bq5 = models.IntegerField(default='')
	bq6 = models.IntegerField(default='')
	bq7 = models.IntegerField(default='')
	bq8 = models.IntegerField(default='')
	bq9 = models.IntegerField(default='')
	bq10 = models.IntegerField(default='')
	date = models.DateTimeField(auto_now_add=True)
	bresult = models.IntegerField(default='0',null=True)

class DmAfter(models.Model):
	uname = models.CharField(max_length=40,null=True)
	aq1 = models.IntegerField(default='')
	aq2 = models.IntegerField(default='')
	aq3 = models.IntegerField(default='')
	aq4 = models.IntegerField(default='')
	aq5 = models.IntegerField(default='')
	aq6 = models.IntegerField(default='')
	aq7 = models.IntegerField(default='')
	aq8 = models.IntegerField(default='')
	aq9 = models.IntegerField(default='')
	aq10 = models.IntegerField(default='')
	date = models.DateTimeField(auto_now_add=True)
	aresult = models.IntegerField(default='0',null=True)
	before2 = models.IntegerField(default='0',null=True)
	alertresult = models.IntegerField(default='0',null=True)
	riskresult = models.IntegerField(default='0',null=True)


class satisfied(models.Model):
	sq1 = models.IntegerField(default='')
	sq2 = models.IntegerField(default='')
	sq3 = models.IntegerField(default='')
	sq4 = models.IntegerField(default='')
	sq5 = models.IntegerField(default='')
	advice = models.CharField(max_length=300,null=True)
	date = models.DateTimeField(auto_now_add=True)
	sresult = models.IntegerField(default='0',null=True)