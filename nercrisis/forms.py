from django.forms import ModelForm
from .models import Report
from django import forms
from django.contrib.auth.models import User


class ReportForm(ModelForm):
	class Meta:
		model = Report
		fields = ['text', 'source', 'what', 'where', 'who', 'when']