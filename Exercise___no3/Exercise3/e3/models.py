# from django.contrib.auth.models import User
from django.db import models


class RouterModel(models.Model):

	idno		=models.AutoField(primary_key=True)
	r_name		=models.CharField(max_length=30)
	r_ip		=models.FloatField(unique=True)
	r_type		=models.CharField(max_length=30)
