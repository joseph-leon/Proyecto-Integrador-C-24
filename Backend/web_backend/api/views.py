##Importando librerias
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Usuario, Titulo, Eslogan, Parrafoobjetivos,
    Subobjetivo1, Subobjetivo2, Tec1, Tec2, Tec3, 
    Tec4, Contacto
)

from .serializers import (
    UsuarioSerializer, TituloSerializer, EsloganSerializer,
    ParrafoobjetivosSerializer,
    Subobjetivo1Serializer, Subobjetivo2Serializer, 
    Tec1Serializer, Tec2Serializer, Tec3Serializer, 
    Tec4Serializer, ContactoSerializer

)
class IndexView(APIView):
    
    def get(self, request):
        context = {
            'ok':True,
            'message': 'El servidor esta activo'
        }
        return Response(context)
    
class UsuarioView(APIView):
    def get(self, request):
        dataUsuario = Usuario.objects.all()
        serUsuario = UsuarioSerializer(dataUsuario, many=True)
        context  = {
            'ok':True,
            'content': serUsuario.data
        }
        return Response(context)

    def post(self,request):
        serUsuario = UsuarioSerializer(data=request.data)
        serUsuario.is_valid(raise_exception=True)
        serUsuario.save()
        
        return Response(serUsuario.data)

class UsuarioDetailView(APIView):
    #obtiene
    def get(self,request,usuario_id):
        dataUsuario = Usuario.objects.get(pk=usuario_id)
        serUsuario = UsuarioSerializer(dataUsuario)
        return Response(serUsuario.data)
    #actualizacion por id
    def put(self,request,usuario_id):
        dataUsuario= Usuario.objects.get(pk=usuario_id)
        serUsuario = UsuarioSerializer(dataUsuario,data=request.data)
        serUsuario.is_valid(raise_exception=True)
        serUsuario.save()
        return Response(serUsuario.data)
    #elimina
    def delete(self,request,usuario_id):
        dataUsuario = Usuario.objects.get(pk=usuario_id)
        serUsuario = UsuarioSerializer(dataUsuario)
        dataUsuario.delete()
        return Response(serUsuario.data)


class TituloView(APIView):

    def get(self, request):
        dataTitulo = Titulo.objects.all()
        serTitulo= TituloSerializer(dataTitulo, many=True)
        return Response(serTitulo.data)
        ##context  = {
        ##    'ok':True,
        ##    'content': serTitulo.data
        ##}


    def post(self,request):
        serTitulo = TituloSerializer(data=request.data)
        serTitulo.is_valid(raise_exception=True)
        serTitulo.save()
        return Response(serTitulo.data)

class TituloDetailView(APIView):

    #obtiene
    def get(self,request,titulo_id):
        dataTitulo = Titulo.objects.get(pk=titulo_id)
        serTitulo = TituloSerializer(dataTitulo)
        return Response(serTitulo.data)

    #actualizacion por id
    def put(self,request,titulo_id):
        dataTitulo = Titulo.objects.get(pk=titulo_id)
        serTitulo = TituloSerializer(dataTitulo,data=request.data)
        serTitulo.is_valid(raise_exception=True)
        serTitulo.save()
        return Response(serTitulo.data)
    #elimina
    def delete(self,request,titulo_id):
        dataTitulo = Titulo.objects.get(pk=titulo_id)
        serTitulo = TituloSerializer(dataTitulo)
        dataTitulo.delete()
        return Response(serTitulo.data)


class EsloganView(APIView):
    def get(self, request):
        dataEslogan = Eslogan.objects.all()
        serEslogan= EsloganSerializer(dataEslogan, many=True)
        return Response(serEslogan.data)

    def post(self,request):
        serEslogan = EsloganSerializer(data=request.data)
        serEslogan.is_valid(raise_exception=True)
        serEslogan.save()
        
        return Response(serEslogan.data)
    

class EsloganDetailView(APIView):
    #obtiene
    def get(self,request,eslogan_id):
        dataEslogan = Eslogan.objects.get(pk=eslogan_id)
        serEslogan = EsloganSerializer(dataEslogan)
        return Response(serEslogan.data)
    #actualizacion por id
    def put(self,request,eslogan_id):
        dataEslogan = Eslogan.objects.get(pk=eslogan_id)
        serEslogan = EsloganSerializer(dataEslogan,data=request.data)
        serEslogan.is_valid(raise_exception=True)
        serEslogan.save()
        return Response(serEslogan.data)
    #elimina
    def delete(self,request,eslogan_id):
        dataEslogan = Eslogan.objects.get(pk=eslogan_id)
        serEslogan = EsloganSerializer(dataEslogan)
        dataEslogan.delete()
        return Response(serEslogan.data)


class ParrafoobjetivosView(APIView):
    def get(self, request):
        dataParrafoobjetivos = Parrafoobjetivos.objects.all()
        serParrafoobjetivos = ParrafoobjetivosSerializer(dataParrafoobjetivos, many=True)
        return Response(serParrafoobjetivos.data)

    def post(self,request):
        serParrafoobjetivos = ParrafoobjetivosSerializer(data=request.data)
        serParrafoobjetivos.is_valid(raise_exception=True)
        serParrafoobjetivos.save()
        return Response(serParrafoobjetivos.data)

#########################
class ParrafoobjetivosDetailView(APIView):
    #obtiene
    def get(self,request,parrafoobjetivos_id):
        dataParrafoobjetivos = Parrafoobjetivos.objects.get(pk=parrafoobjetivos_id)
        serParrafoobjetivos = ParrafoobjetivosSerializer(dataParrafoobjetivos)
        return Response(serParrafoobjetivos.data)
    #actualizacion por id
    def put(self,request,parrafoobjetivo_id):
        dataParrafoobjetivos = Parrafoobjetivos.objects.get(pk=parrafoobjetivo_id)
        serParrafoobjetivos = ParrafoobjetivosSerializer(dataParrafoobjetivos,data=request.data)
        serParrafoobjetivos.is_valid(raise_exception=True)
        serParrafoobjetivos.save()
        return Response(serParrafoobjetivos.data)
    #elimina
    def delete(self,request,parrafoobjetivos_id):
        dataParrafoobjetivos = Parrafoobjetivos.objects.get(pk=parrafoobjetivos_id)
        serParrafoobjetivos = ParrafoobjetivosSerializer(dataParrafoobjetivos)
        dataParrafoobjetivos.delete()
        return Response(serParrafoobjetivos.data)


class Subobjetivo1View(APIView):
    def get(self, request):
        dataSubobjetivo1 = Subobjetivo1.objects.all()
        serPSubobjetivo1 = Subobjetivo1Serializer(dataSubobjetivo1, many=True)
        return Response(serPSubobjetivo1.data)

    def post(self,request):
        serSubobjetivo1 = Subobjetivo1Serializer(data=request.data)
        serSubobjetivo1.is_valid(raise_exception=True)
        serSubobjetivo1.save()


class Subobjetivo1DetailView(APIView):
    #obtiene
    def get(self,request,subobjetivo1_id):
        dataSubobjetivo1 = Subobjetivo1.objects.get(pk=subobjetivo1_id)
        serSubobjetivo1 = Subobjetivo1Serializer(dataSubobjetivo1)
        return Response(serSubobjetivo1.data)
    #actualizacion por id
    def put(self,request,subobjetivo1_id):
        dataSubobjetivo1 = Subobjetivo1.objects.get(pk=subobjetivo1_id)
        serSubobjetivo1 = Subobjetivo1Serializer(dataSubobjetivo1,data=request.data)
        serSubobjetivo1.is_valid(raise_exception=True)
        serSubobjetivo1.save()
        return Response(serSubobjetivo1.data)
    #elimina
    def delete(self,request,subobjetivo1_id):
        dataSubobjetivo1 = Subobjetivo1.objects.get(pk=subobjetivo1_id)
        serSubobjetivo1 = Subobjetivo1Serializer(dataSubobjetivo1)
        serSubobjetivo1.delete()
        return Response(serSubobjetivo1.data)
##############

class Subobjetivo2View(APIView):
    def get(self, request):
        dataSubobjetivo2 = Subobjetivo2.objects.all()
        serPSubobjetivo2 = Subobjetivo2Serializer(dataSubobjetivo2, many=True)
        return Response(serPSubobjetivo2.data)

    def post(self,request):
        serSubobjetivo2 = Subobjetivo2Serializer(data=request.data)
        serSubobjetivo2.is_valid(raise_exception=True)
        serSubobjetivo2.save()


class Subobjetivo2DetailView(APIView):
    #obtiene
    def get(self,request,subobjetivo2_id):
        dataSubobjetivo2 = Subobjetivo2.objects.get(pk=subobjetivo2_id)
        serSubobjetivo2 = Subobjetivo2Serializer(dataSubobjetivo2)
        return Response(serSubobjetivo2.data)
    #actualizacion por id
    def put(self,request,subobjetivo2_id):
        dataSubobjetivo2 = Subobjetivo2.objects.get(pk=subobjetivo2_id)
        serSubobjetivo2 = Subobjetivo2Serializer(dataSubobjetivo2,data=request.data)
        serSubobjetivo2.is_valid(raise_exception=True)
        serSubobjetivo2.save()
        return Response(serSubobjetivo2.data)
    #elimina
    def delete(self,request,subobjetivo2_id):
        dataSubobjetivo2 = Subobjetivo2.objects.get(pk=subobjetivo2_id)
        serSubobjetivo2 = Subobjetivo2Serializer(dataSubobjetivo2)
        serSubobjetivo2.delete()
        return Response(serSubobjetivo2.data)

class Tec1View(APIView):
    def get(self, request):
        dataTec1 = Tec1.objects.all()
        serTec1 = Tec1Serializer(dataTec1, many=True)
        return Response(serTec1.data)

    def post(self,request):
        serTec1 = Tec1Serializer(data=request.data)
        serTec1.is_valid(raise_exception=True)
        serTec1.save()

class Tec1DetailView(APIView):
    #obtiene
    def get(self,request,tec1_id):
        dataTec1 = Tec1.objects.get(pk=tec1_id)
        serTec1 = Tec1Serializer(dataTec1)
        return Response(serTec1.data)
    #actualizacion por id
    def put(self,request,tec1_id):
        dataTec1 = Tec1.objects.get(pk=tec1_id)
        serTec1 = Tec1Serializer(dataTec1,data=request.data)
        serTec1.is_valid(raise_exception=True)
        serTec1.save()
        return Response(serTec1.data)
    #elimina
    def delete(self,request,tec1_id):
        dataTec1 = Tec1.objects.get(pk=tec1_id)
        serTec1 = Tec1Serializer(dataTec1)
        dataTec1.delete()
        return Response(serTec1.data)


class Tec2View(APIView):
    def get(self, request):
        dataTec2 = Tec2.objects.all()
        serTec2 = Tec2Serializer(dataTec2, many=True)
        return Response(serTec2.data)

    def post(self,request):
        serTec2 = Tec2Serializer(data=request.data)
        serTec2.is_valid(raise_exception=True)
        serTec2.save()


class Tec2DetailView(APIView):
    #obtiene
    def get(self,request,tec2_id):
        dataTec2 = Tec1.objects.get(pk=tec2_id)
        serTec2 = Tec2Serializer(dataTec2)
        return Response(serTec2.data)
    #actualizacion por id
    def put(self,request,tec2_id):
        dataTec2 = Tec2.objects.get(pk=tec2_id)
        serTec2 = Tec2Serializer(dataTec2,data=request.data)
        serTec2.is_valid(raise_exception=True)
        serTec2.save()
        return Response(serTec2.data)
    #elimina
    def delete(self,request,tec2_id):
        dataTec2 = Tec2.objects.get(pk=tec2_id)
        serTec2 = Tec2Serializer(dataTec2)
        dataTec2.delete()
        return Response(serTec2.data)

class Tec3View(APIView):
    def get(self, request):
        dataTec3 = Tec3.objects.all()
        serTec3 = Tec3Serializer(dataTec3, many=True)
        return Response(serTec3.data)

    def post(self,request):
        serTec3 = Tec3Serializer(data=request.data)
        serTec3.is_valid(raise_exception=True)
        serTec3.save()

class Tec3DetailView(APIView):
    #obtiene
    def get(self,request,tec3_id):
        dataTec3 = Tec3.objects.get(pk=tec3_id)
        serTec3 = Tec3Serializer(dataTec3)
        return Response(serTec3.data)
    #actualizacion por id
    def put(self,request,tec3_id):
        dataTec3 = Tec3.objects.get(pk=tec3_id)
        serTec3 = Tec3Serializer(dataTec3,data=request.data)
        serTec3.is_valid(raise_exception=True)
        serTec3.save()
        return Response(serTec3.data)
    #elimina
    def delete(self,request,tec3_id):
        dataTec3 = Tec3.objects.get(pk=tec3_id)
        serTec3 = Tec3Serializer(dataTec3)
        dataTec3.delete()
        return Response(serTec3.data)

class Tec4View(APIView):
    def get(self, request):
        dataTec4 = Tec4.objects.all()
        serTec4 = Tec4Serializer(dataTec4, many=True)
        return Response(serTec4.data)

    def post(self,request):
        serTec4 = Tec4Serializer(data=request.data)
        serTec4.is_valid(raise_exception=True)
        serTec4.save()

class Tec4DetailView(APIView):
    #obtiene
    def get(self,request,tec4_id):
        dataTec4 = Tec4.objects.get(pk=tec4_id)
        serTec4 = Tec4Serializer(dataTec4)
        return Response(serTec4.data)
    #actualizacion por id
    def put(self,request,tec4_id):
        dataTec4 = Tec4.objects.get(pk=tec4_id)
        serTec4 = Tec4Serializer(dataTec4,data=request.data)
        serTec4.is_valid(raise_exception=True)
        serTec4.save()
        return Response(serTec4.data)
    #elimina
    def delete(self,request,tec4_id):
        dataTec4 = Tec4.objects.get(pk=tec4_id)
        serTec4 = Tec4Serializer(dataTec4)
        dataTec4.delete()
        return Response(serTec4.data)

class ContactoView(APIView):
    def get(self, request):
        dataContacto = Contacto.objects.all()
        serContacto = ContactoSerializer(dataContacto, many=True)
        return Response(serContacto.data)

    def post(self,request):
        serContacto = ContactoSerializer(data=request.data)
        serContacto.is_valid(raise_exception=True)
        serContacto.save()

class ContactoDetailView(APIView):
    #obtiene
    def get(self,request,contacto_id):
        dataContacto = Contacto.objects.get(pk=contacto_id)
        serContacto = ContactoSerializer(dataContacto)
        return Response(serContacto.data)
    #actualizacion por id
    def put(self,request,contacto_id):
        dataContacto = Contacto.objects.get(pk=contacto_id)
        serContacto = ContactoSerializer(dataContacto,data=request.data)
        serContacto.is_valid(raise_exception=True)
        serContacto.save()
        return Response(serContacto.data)
    #elimina
    def delete(self,request,contacto_id):
        dataContacto = Contacto.objects.get(pk=contacto_id)
        serContacto = ContactoSerializer(dataContacto)
        dataContacto.delete()
        return Response(serContacto.data)