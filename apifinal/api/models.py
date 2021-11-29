from django.db import models

# Create your models here.
class Usuario(models.Model):
    Nombre = models.CharField(max_length=50,verbose_name="Nombre")
    Correo = models.CharField(max_length=50,verbose_name="Correo")
    contrasena = models.CharField(max_length=50,null= True,blank=True,verbose_name="password")
    

    def __str__(self):
        return self.Nombre