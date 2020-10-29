from rest_framework import serializers
from .models import idModel, ageModel
#used serializers to convert the complex model instances to native Python datatypes and those can be easily rendered into JSON


class IDSerializer(serializers.ModelSerializer):
    values=serializers.JSONField()
    class Meta:
        model = idModel
        fields = '__all__'

class AgeSerializer(serializers.ModelSerializer):
    values=serializers.JSONField()
    class Meta:
        model = ageModel
        fields = '__all__'