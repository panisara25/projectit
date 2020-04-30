from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    com_img = models.ImageField(default='userprofile.png', upload_to='company_img',null=True)
    company_name = models.CharField(max_length=150)
    company_detail = models.TextField()
    company_address = models.TextField(null=True)
    benifit = models.TextField(null=True)
    contact = models.TextField(null=True)
    prove = models.ImageField(default='userprofile.png',upload_to='prove/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.company_name}({self.user.username})'
    
    def save(self, *args, **kwargs):
        super(CompanyProfile,self).save(*args, **kwargs)
        
        img = Image.open(self.com_img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.com_img.path)
    
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='userprofile.png', upload_to='upload')
    resume = resume = models.ImageField(default='userprofile.png',upload_to='Resume/', null=True, blank=True)
    about =  models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
            



     


