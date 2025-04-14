from rest_framework import serializers
from .models import Item  # adjust to match your model name

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name'] 
