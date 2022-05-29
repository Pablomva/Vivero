from django.db import models
from django.contrib.auth.models import User

class Arboles(models.Model):
    familia=models.CharField(max_length=255)
    nombre_cientifico=models.CharField(max_length=255)
    nombre_comun=models.CharField(max_length=255)
    tipo_canopia=models.CharField(max_length=255)
    forma=models.CharField(max_length=255)
    altura_media_en_metros=models.FloatField()

    def __str__(self):
        return f"Familia:{self.familia} - Nombre cientifico:{self.nombre_cientifico} - Nombre comun:{self.nombre_comun} "

    class Meta:
        verbose_name = "Arboles"
        verbose_name_plural = "Arboles"

class Arbustos(models.Model):
    familia=models.CharField(max_length=255)
    nombre_cientifico=models.CharField(max_length=255)
    nombre_comun=models.CharField(max_length=255)
    tipo_canopia=models.CharField(max_length=255)
    forma=models.CharField(max_length=255)
    altura_media_en_metros=models.FloatField()

    def __str__(self):
        return f"Familia:{self.familia} - Nombre cientifico:{self.nombre_cientifico} - Nombre comun:{self.nombre_comun} "

    class Meta:
        verbose_name = "Arbustos"
        verbose_name_plural = "Arbustos"

class Herbaceas(models.Model):
    familia=models.CharField(max_length=255)
    nombre_cientifico=models.CharField(max_length=255)
    nombre_comun=models.CharField(max_length=255)
    tipo_canopia=models.CharField(max_length=255)
    forma=models.CharField(max_length=255)
    altura_media_en_metros=models.FloatField()

    def __str__(self):
        return f"Familia:{self.familia} - Nombre cientifico:{self.nombre_cientifico} - Nombre comun:{self.nombre_comun} "

    class Meta:
        verbose_name = "Herbaceas"
        verbose_name_plural = "Herbaceas"

class Semillas(models.Model):
    familia=models.CharField(max_length=255)
    nombre_cientifico=models.CharField(max_length=255)
    nombre_comun=models.CharField(max_length=255)
    caracteristicas=models.TextField()

    def __str__(self):
        return f"Familia:{self.familia} - Nombre cientifico:{self.nombre_cientifico} - Nombre comun:{self.nombre_comun} "

    class Meta:
        verbose_name = "Semillas"
        verbose_name_plural = "Semillas"

class Usuarios(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.EmailField()
    pais=models.CharField(max_length=255)
    provincia=models.TextField()
    ciudad=models.CharField(max_length=255)

    def __str__(self):
        return f"Nombre:{self.nombre} - Apellido:{self.apellido} - E-mail:{self.email} "

    class Meta:
        verbose_name = "Usuarios"
        verbose_name_plural = "Usuarios" 
    


    








