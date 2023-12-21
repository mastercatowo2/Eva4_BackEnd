from rest_framework import serializers
from Mondongo.models import Estudiante
from Mondongo.models import Ramo
from Mondongo.models import Docente

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class RamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ramo
        fields = '__all__'                