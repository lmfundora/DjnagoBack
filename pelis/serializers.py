from rest_framework import serializers
from pelis.models import PelisModel, LabelsModel


class PelisSerializer(serializers.ModelSerializer):
    class Meta:
        model = PelisModel
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelsModel
        fields = '__all__'