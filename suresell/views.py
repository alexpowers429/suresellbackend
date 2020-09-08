from django.shortcuts import render
from rest_framework import generics
from .serializers import CarSerializer, FeatureSerializer
from .models import Car, SellingFeatures
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_class = (IsAuthenticatedOrReadOnly)


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_class = (IsAuthenticatedOrReadOnly)


class FeatureList(generics.ListCreateAPIView):
    queryset = SellingFeatures.objects.all()
    serializer_class = FeatureSerializer
    permission_class = (IsAuthenticatedOrReadOnly)


class FeatureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SellingFeatures.objects.all()
    serializer_class = FeatureSerializer
    permission_class = (IsAuthenticatedOrReadOnly)
