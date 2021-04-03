from django.db import models

# Create your models here.
class Task(models.Model):
    task_id = models.CharField(max_length=60)
    task_name = models.CharField(max_length=60)
    task_description=models.CharField(max_length=100,default="")
    task_priority=models.CharField(max_length=100,default=1)
    image= models.ImageField(upload_to="myapi/images",default="")
    def __str__(self):
        return self.name