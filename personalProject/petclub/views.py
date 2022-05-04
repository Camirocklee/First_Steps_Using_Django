from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from petclub.models import(
    Person,
    Pet,
)
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)

class HelloWorld(APIView): #Clase(PuntoDeEntrada):
    def get(self,request): # verbo de la peticion como un metodo
        #logica asociada al endpoint
        return Response(data="Hello World! ", status=200) #respuesta del servicio

    def patch(self,request):
        return Response(data="Hola gente estoy en el patch" , status=200)
    def delete(self,request):
        return Response(data="Hola gente estoy en el delete! ", status=200)
    def post(self,request):
        return Response(data="Hola gente estoy en el post! ", status=200)

class PersonAPI(APIView):
    def get(self,request):
        personas = [person.rut for person in Person.objects.all()]
        if not personas:
            return Response(data="Estoy en el get, aun no hay personas creadas", status=200)

        return Response(personas) 
    def patch(self,request):
        return Response(data="Estoy en el patch de PersonAPI" , status=200)
    def delete(self,request):
        return Response(data="Estoy en el delete de PersonAPI ", status=200)
    def post(self,request):
        return Response(data="Estoy en el post de PersonAPI", status=200)

class PetAPI(APIView):
    def get(self,request):
        pets = [pet.rut for pet in Pet.objects.all()]
        if not pets:
            return Response(data="Estoy en el get, aun no hay pets creadas", status=200)

        return Response(pets) 
    def patch(self,request):
        return Response(data="Estoy en el patch de PetsAPI" , status=200)
    def delete(self,request):
        return Response(data="Estoy en el delete de PetsAPI ", status=200)
    def post(self,request):
        return Response(data="Estoy en el post de PetsAPI", status=200)


class PetListAPIView(ListAPIView):
    def get(self,request):
        return Response(data="Hola a todos estas son mis mascotas", status = 200)


class PetAPIView(RetrieveAPIView):
    def get(self,request):
        return Response(data="Hola gente estoy en el post", status=200) #Agregar a la url, cada app debe tener su propia url
class HelloWorldOnlyGet(RetrieveAPIView):
    pass
# Create your views here.
