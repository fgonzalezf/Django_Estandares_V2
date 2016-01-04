#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

class ConsultaFormulario(forms.Form):
     codigo =forms.CharField(widget = forms.TextInput(attrs={'class' : 'myfieldclass'}),required=True,label="Código asignado al estandar en consulta")
     nombre= forms.CharField(widget = forms.TextInput(attrs={'class' : 'myfieldclass'}),max_length=200,label="Nombre del estandar")
     contibuidor= forms.CharField(widget = forms.TextInput(attrs={'class' : 'myfieldclass'}),max_length=200, label="Nombre de quien hace la contribución")
     correo= forms.EmailField(widget = forms.TextInput(attrs={'class' : 'myfieldclass'}),max_length=200, label="Correo electronico")
     comentario= forms.CharField(widget=forms.Textarea(attrs={'class' : 'myfieldclass'}) ,label="Comentarios y sugerencias al estandar en consulta")
     adjunto = forms.Field(widget = forms.FileInput(attrs={'class' : 'myfieldclass'}),required=False)
     def __unicode__(self):
        return self.nombre