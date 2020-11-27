from django.db import models
choices=[
    ('1','Completed'),
    ('2','Not Completed')
]
# Create your models here.
class MyModel(models.Model):
    title = models.CharField(max_length=255)
    choice=models.CharField(max_length=100,choices=choices,default="")

