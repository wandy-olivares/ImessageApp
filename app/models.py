from django.db import models

# Create your models here.
class User(models.Model):
    number_user = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.number_user
    
    
class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clave = models.CharField(max_length=50)
    name_user = models.CharField(max_length=100)
    friend = models.CharField(max_length=100, default=False)
    
    
    def __str__(self) -> str:
        return self.name_user

class Chat_User(models.Model):
    mensage = models.CharField(max_length=100)