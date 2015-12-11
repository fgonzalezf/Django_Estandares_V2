from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Documento,Versiones,FormularioConsulta
from django.core.urlresolvers import reverse_lazy
from django.core.mail import EmailMessage
from django.contrib import messages
class Home(TemplateView):
    template_name = "index.html"

class Tematicas(TemplateView):
    template_name = "tematicas.html"


class ListaDocumentos(TemplateView):
    def post(self, request, *args, **kwargs):
        busquedaTipo = request.POST['Tematica'].upper()
        busquedaTematica= request.POST['Area'].upper()
        Documentos= Documento.objects.filter(tipo__contains=busquedaTipo)
        Documentosfin= Documentos.filter(tematica__contains=busquedaTematica)
        datos=[]
        if Documentosfin:
            for documento in Documentosfin:
                versionesAnt= Versiones.objects.filter(codigo=documento.pk)
                datos.append(dict([(documento,versionesAnt)]))
            for dato in datos:
                for documento,version in dato.items():
                    for doc in version:
                        print doc.url

        return render(request,'consulta.html',{'datos':datos})


class FormularioConsultaView(CreateView):
    template_name = 'Formulario.html'
    model = FormularioConsulta
    fields = '__all__'
    success_message="Mensaje"
    success_url = reverse_lazy('Home')
    def post(self, request, *args, **kwargs):
        email = EmailMessage('Hello', 'World', to=['pachecofgf@gmail.com'])
        email.send()


class Busqueda(TemplateView):
    def post(self,request,*args,**kwargs):
        buscar = request.POST['buscar']
        nombreDoc = Documento.objects.filter(nombre__contains=buscar)
        codigoDoc= Documento.objects.filter(codigo__contains=buscar)
        documentos=[]
        datos=[]
        if nombreDoc:
            for doc in nombreDoc:
                documentos.append(doc)
        elif codigoDoc:
            for doc in codigoDoc:
                documentos.append(doc)

        if documentos:
            for documento in documentos:
                versionesAnt= Versiones.objects.filter(codigo=documento.pk)
                datos.append(dict([(documento,versionesAnt)]))
        return render(request,"Busqueda.html",{'datos':datos})

class DocConsulta(TemplateView):
    def post(self,request,*args,**kwargs):
        nombreDoc = Documento.objects.filter(discusion__contains="SI")
        documentos=[]
        datos=[]
        if nombreDoc:
            for doc in nombreDoc:
                documentos.append(doc)
        if documentos:
            for documento in documentos:
                versionesAnt= Versiones.objects.filter(codigo=documento.pk)
                datos.append(dict([(documento,versionesAnt)]))
        return render(request,"docConsulta.html",{'datos':datos})

# Create your views here.
# application/msword
