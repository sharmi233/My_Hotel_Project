from rest_framework import serializers
from .models import Room # Unga model name 'Room' nu nenaikiren

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__' # Ella details-aiyum (Name, Price, etc.) anuppum