from django.db import models


class RouterModel(models.Model):

	idno		=models.AutoField(primary_key=True)
	router_name	=models.CharField(max_length=30)
	

