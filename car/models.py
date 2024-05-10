from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

    
    
    
class Car(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.CharField(max_length=200,default=0)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    image = models.ImageField(blank = True,null = True)
    
    
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
        
        
    

    
