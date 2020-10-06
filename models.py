from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122, null= True)
    email = models.CharField(max_length=122, null= True)
    phone = models.CharField(max_length=12, null= True)
    desc = models.CharField(max_length=50, null=True)
    date = models.DateField(auto_now_add=True,null= True)

    def __str__(self):
        return self.name
    