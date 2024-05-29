from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

class GetPeople(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class GetPerson(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'

