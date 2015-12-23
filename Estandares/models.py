from django.db import models

class Documento (models.Model):
    nombre= models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    tematica=models.CharField(max_length=100)
    codigo= models.CharField(max_length=100,primary_key=True)
    fechaPublicacion= models.DateField()
    vigencia= models.DateField()
    otrasVersiones = models.CharField(max_length=100)
    discusion = models.CharField(max_length=100)
    url= models.CharField(max_length=250)
    def __unicode__(self):
        return self.codigo
class Versiones (models.Model):
    codigo = models.ManyToManyField(Documento)
    nombre= models.CharField(max_length=200)
    fecha= models.DateField()
    url=models.CharField(max_length=250)
    def __unicode__(self):
        return self.nombre

class FormularioConsulta(models.Model):
    codigo =models.ForeignKey(Documento)
    contibuidor= models.CharField(max_length=200)
    institucion= models.CharField(max_length=200)
    correo= models.EmailField(max_length=200)
    comentario= models.TextField()
    def __unicode__(self):
        return self.contibuidor



# Create your models here.
