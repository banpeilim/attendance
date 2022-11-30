from rest_framework import serializers
from .models import Flight, Queue, Inventory

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['time', 'destination', 'flight', 'gate', 'status']


class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = ['name']


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['storeid', 'productid', 'udpip', 'stock', 'signal']