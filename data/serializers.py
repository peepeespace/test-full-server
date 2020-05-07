from rest_framework import serializers
from data.models import ControlState, ToolState

class ControlStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlState
        fields = '__all__'

class ToolStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolState
        fields = '__all__'