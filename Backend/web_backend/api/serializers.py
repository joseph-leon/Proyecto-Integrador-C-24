from rest_framework import serializers

from .models import (
    Usuario, Titulo, Eslogan, Parrafoobjetivos,
    Subobjetivo1, Subobjetivo2, Tec1, Tec2, Tec3, 
    Tec4, Contacto
)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class TituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titulo
        fields= '__all__'

class EsloganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eslogan
        fields= '__all__'

class ParrafoobjetivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parrafoobjetivos
        fields= '__all__'

class Subobjetivo1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subobjetivo1
        fields= '__all__'

class Subobjetivo2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subobjetivo2
        fields= '__all__'

class Tec1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tec1
        fields= '__all__'

class Tec2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tec2
        fields= '__all__'

class Tec3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tec3
        fields= '__all__'

class Tec4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tec4
        fields= '__all__'

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields= '__all__'