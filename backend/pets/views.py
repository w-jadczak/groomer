from django.shortcuts import render
from rest_framework import generics
from pets.models import Pet
from pets.serializers import PetSerializer

class PetCreateView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetListView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetRetrieveView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetUpdateView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetDestroyView(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer