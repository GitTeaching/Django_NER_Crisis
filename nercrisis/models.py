from django.db import models
from django.contrib.auth.models import User


class Report(models.Model):
	SOURCE = (('File', 'File'), ('Twitter', 'Twitter'))
	text = models.TextField(max_length=2500, null=True)
	source = models.CharField(max_length=20, null=True, choices=SOURCE)
	what = models.CharField(max_length=200)
	where = models.CharField(max_length=200)
	when = models.CharField(max_length=200)
	who = models.CharField(max_length=200)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.text
