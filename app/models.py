from django.db import models

class MarketingSolution(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="marketing/")

    
    def __str__(self):
        return self.title
    

    
class Portfolio(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to="portfolio/")
    
    def __str__(self):
        return self.title
    
    
class Service(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to='service/')
    
    def __str__(self):
        return self.title

    
class Coomessage(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to='service/')
    
    def __str__(self):
        return self.title

    
class Teammembers(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='service/')
    
    def __str__(self):
        return self.title

    
class Creative(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='service/')
    
    def __str__(self):
        return self.title
    
    
class Reviews(models.Model):
    title=models.CharField(max_length=50)
    text=models.TextField()
    image=models.ImageField(upload_to="reviews/")
    
    def __str__(self):
        return self.title


class Desinglist(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='desings/')
    
    def __str__(self):
        return self.title
    
    
class coreservice(models.Model):
    title=models.CharField(max_length=50)
    text=models.TextField()
    image=models.ImageField(upload_to="core/")
    
    def __str__(self):
        return self.title