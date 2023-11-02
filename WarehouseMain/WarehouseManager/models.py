from django.db import models

# Create your models here.

class Transport(models.Model):
	name=models.CharField(max_length=50)
	capacity=models.IntegerField(default=0)

	def __str__(self):
		return self.name 


class TransportType(models.Model):
	name=models.CharField(max_length=50)
	@staticmethod	
	def get():
		objects=TransportType.objects.all()
		list_of_types=[]
		
		for object_get in objects :
				selection=[]
				selection.append(object_get.name)
				selection.append(object_get.name)
				list_of_types.append(tuple(selection))
		return list_of_types

	def __str__(self):
		return self.name

class Car_routes(models.Model):
	from_T=models.CharField(max_length=50)
	to_T=models.CharField(max_length=50)
	name=models.CharField(max_length=100,null=True)
	@staticmethod	
	def get():
		objects=Car_routes.objects.all()
		list_of_types=[]
		
		for object_get in objects :
				selection=[]
				selection.append(object_get.name)
				selection.append(object_get.name)
				list_of_types.append(tuple(selection))
		return list_of_types
	def save(self, *args, **kwargs):
		self.name=str(self.from_T)+"-"+str(self.to_T)
		super().save(*args, **kwargs)  
	def __str__(self):
		return self.name

class Naval_routes(models.Model):
	from_T=models.CharField(max_length=50)
	to_T=models.CharField(max_length=50)
	name=models.CharField(max_length=100,null=True)
	@staticmethod	
	def get():
		objects=Naval_routes.objects.all()
		list_of_types=[]
		
		for object_get in objects :
				selection=[]
				selection.append(object_get.name)
				selection.append(object_get.name)
				list_of_types.append(tuple(selection))
		return list_of_types
	def save(self, *args, **kwargs):
		self.name=str(self.from_T)+"-"+str(self.to_T)
		super().save(*args, **kwargs)  
		
		
	def __str__(self):
		return self.name


class CarTransport(Transport):
		CarTransportType=models.CharField(choices=TransportType.get(),max_length=100)
		Parked=models.BooleanField()
		Route=models.CharField(choices=Car_routes.get(),max_length=100)

class NavalTransport(Transport):
		NavalTransportType=models.CharField(choices=TransportType.get(),max_length=100)	
		Docked=models.BooleanField()
		Route=models.CharField(choices=Naval_routes.get(),max_length=100)
		