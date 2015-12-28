__author__ = 'fernando'

from django import forms

class ConsultaFormulario(forms.Form):
     codigo =forms.CharField(required=True,label="Codigo asignado al estandar en consulta")
     nombre= forms.CharField(max_length=200,label="Nombre del estandar")
     contibuidor= forms.CharField(max_length=200, label="Nombre de quien hace la contribucion")
     correo= forms.EmailField(max_length=200, label="Correo electronico")
     comentario= forms.CharField(widget=forms.Textarea ,label="Comentarios y sugerencias al estandar en consulta")
     adjunto = forms.Field(widget = forms.FileInput,required=False)
     def __unicode__(self):
        return self.nombre