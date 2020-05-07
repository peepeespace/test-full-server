from django.shortcuts import render

from data.models import ControlState, ToolState
from data.serializers import ControlStateSerializer, ToolStateSerializer

from rest_framework import generics


class ControlStateList(generics.ListCreateAPIView):
    queryset = ControlState.objects.all()
    serializer_class = ControlStateSerializer

class ToolStateList(generics.ListCreateAPIView):
    queryset = ToolState.objects.all()
    serializer_class = ToolStateSerializer