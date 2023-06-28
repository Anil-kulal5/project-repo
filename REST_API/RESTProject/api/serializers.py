from rest_framework import serializers
from .models import Customer


class CustomerSerializers(serializers.HyperlinkedModelSerializer):
    
    # ModelOBj ==> Python Native
    # Python Natave ==> Modelobj
    
    class Meta:
        model = Customer
        fields = "__all__"