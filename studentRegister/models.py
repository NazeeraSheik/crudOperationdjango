from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Position(models.Model):
	title=models.CharField(max_length=50)
	def __str__(self):
		return self.title
class Student(models.Model):
	fullname=models.CharField(max_length=100,unique=True,error_messages={'unique':"this name is already registered"})
	studentid=models.CharField(max_length=10,unique=True)
	mobile=models.CharField(max_length=15)
	position=models.ForeignKey(Position,on_delete=models.CASCADE)
