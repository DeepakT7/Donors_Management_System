from django.db import models

# Create your models here.

class Donor(models.Model):
    name = models.CharField(max_length=200, null =True)
    phone = models.CharField(max_length=200, null =True)
    email = models.CharField(max_length=200, null =True)
    date_created = models.DateTimeField(auto_now_add=True,null =True)


    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null =True)

    def __str__(self):
        return self.name

class Donations(models.Model):
    
    name = models.CharField(max_length=200,null =True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null =True)
    description = models.CharField(max_length=200,null =True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True,null =True)
    tags = models.ManyToManyField(Tag)


class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	donor = models.ForeignKey(Donor, null = True, on_delete = models.SET_NULL)
	donation = models.ForeignKey(Donations, null = True, on_delete = models.SET_NULL) 
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)














