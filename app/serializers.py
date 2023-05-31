from rest_framework import serializers
from .models import *

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'seatNum', 'stuNum']


class DummyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyModel
        fields = ['className', 'classCount']