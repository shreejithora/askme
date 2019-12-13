from django.db import models

# Create your models here.

class UserModel(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    password = models.CharField(max_length=120)
    address = models.CharField(max_length=255, null=True)
    contact = models.CharField(max_length=14, null=True)
    reputation = models.PositiveIntegerField(default=0)

    def __str__(self):
        return(self.name)
