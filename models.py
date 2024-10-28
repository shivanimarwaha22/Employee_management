from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)        
    address = models.TextField()                   
    location = models.CharField(max_length=100)     
    company_type = models.CharField(max_length=50)  
    established_date = models.DateField()  

    def str(self):
        return self.name 

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, related_name='projects', on_delete=models.CASCADE)

    def _str_(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project, related_name='employees')

    def _str_(self):
        return self.name

# Create your models here.
