from django.db import models
from django.core.files import File
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Salary(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class Type_Job(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    
class Gender(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class PostJob(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    type_job = models.ForeignKey(Type_Job,on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True)
    salary = models.ForeignKey(Salary,on_delete=models.CASCADE,null=True)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE,null=True)
    vacancy = models.CharField(max_length=100, null=True)
    contact_com = models.TextField(null=True)
    requirement = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-timestamp","-date_posted"]
        
class Application(models.Model):
    applicant = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    jobpost = models.ForeignKey(PostJob, on_delete=models.CASCADE,related_name='post', blank=True, null=True)
    description = models.TextField()
    date_applied = models.DateTimeField(auto_now=False, auto_now_add=True)
    contact_app = models.TextField( blank=True, null=True)
    
    class Meta:
        ordering = ["date_applied"]
        

        
    

        



        
