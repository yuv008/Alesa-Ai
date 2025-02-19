from rest_framework import serializers
from .models import DreamInterpretation


class DreamInterpretationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DreamInterpretation
        fields = ["id", "dream_description", "interpretation", "created_at"]
        read_only_fields = ["interpretation", "created_at"]
