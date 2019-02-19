from rest_framework import serializers
from restaurants.models import Restaurant

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'opening_time', 'closing_time',]