from django.shortcuts import render
from rest_framework import generics
from .serializers import CarSerializer, FeatureSerializer
from .models import Car, SellingFeatures


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class FeatureList(generics.ListCreateAPIView):
    queryset = SellingFeatures.objects.all()
    serializer_class = FeatureSerializer


class FeatureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SellingFeatures.objects.all()
    serializer_class = FeatureSerializer
