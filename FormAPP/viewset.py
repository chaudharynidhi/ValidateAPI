from rest_framework import viewsets
from .models import idModel, ageModel
from .serializer import IDSerializer, AgeSerializer

""" for creating the CRUD API view using ModelViewSet, used this as the implementation is easier for simple CRUD api as compared to AppViewSet """

class IDViewSets(viewsets.ModelViewSet):
    queryset = idModel.objects.all()
    serializer_class = IDSerializer

class AgeViewSets(viewsets.ModelViewSet):
    queryset = ageModel.objects.all()
    serializer_class = AgeSerializer    