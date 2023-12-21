from django.shortcuts import render
from django.http import JsonResponse

from .serializers import EstudianteSerializer
from .serializers import DocenteSerializer
from .serializers import RamoSerializer

from .models import Estudiante, Ramo, Docente

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView

from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import generics, mixins

#Create your views here.

def employeeView(request):
     emp={
         'id':123,
         'name':'Clark',
         'email':'sup@jl.org',
         'salary':'11000'
     }
     return JsonResponse(emp)

#Lista Estudiante
class ListaEstudiantes(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


    def get(self, request):
        estudiantes = Estudiante.objects.all()
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)



    def post(self, request):
        serializer = EstudianteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Detalles Estudiante
class EstudianteA(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


    def get(self, request, pk):
        estudiante = get_object_or_404(Estudiante, pk=pk)
        serializer = EstudianteSerializer(estudiante)
        return Response(serializer.data)

    def put(self, request, pk):
        estudiante = get_object_or_404(Estudiante, pk=pk)
        serializer = EstudianteSerializer(estudiante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        estudiante = get_object_or_404(Estudiante, pk=pk)
        estudiante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Lista Docentes
class ListaDocentes(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


    def get(self, request):
        docentes = Docente.objects.all()
        serializer = DocenteSerializer(docentes, many=True)
        return Response(serializer.data)
    

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)




    def post(self, request):
        serializer = DocenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Detalles Docente
class DocenteA(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


    def get(self, request, pk):
        docente = get_object_or_404(Docente, pk=pk)
        serializer = DocenteSerializer(docente)
        return Response(serializer.data)

    def put(self, request, pk):
        docente = get_object_or_404(Docente, pk=pk)
        serializer = DocenteSerializer(docente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        docente = get_object_or_404(Docente, pk=pk)
        docente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Lista Ramos
class ListaRamos(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


    def get(self, request):
        ramos = Ramo.objects.all()
        serializer = RamoSerializer(ramos, many=True)
        return Response(serializer.data)

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


    def post(self, request):
        serializer = RamoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Detalles Ramo
class RamoA(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    

    def get(self, request, pk):
        ramo = get_object_or_404(Ramo, pk=pk)
        serializer = RamoSerializer(ramo)
        return Response(serializer.data)

    def put(self, request, pk):
        ramo = get_object_or_404(Ramo, pk=pk)
        serializer = RamoSerializer(ramo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ramo = get_object_or_404(Ramo, pk=pk)
        ramo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)