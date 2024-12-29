from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Contact(models.Model):
    full_name=models.CharField(max_length=250)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    message=CKEditor5Field('Text', config_name='extends')
    


    
    
