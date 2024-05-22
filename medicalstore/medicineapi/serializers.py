from rest_framework import serializers
from medicines.models import medList

class medSerializer(serializers.ModelSerializer):
    class Meta:
        model = medList
        fields = '__all__'