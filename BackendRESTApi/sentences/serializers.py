from rest_framework import serializers
from .models import Sentence


class SentenceListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        sentences = [Sentence(**item) for item in validated_data]
        return Sentence.objects.bulk_create(sentences)

class SentenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sentence
        fields = '__all__'
        list_serializer_class = SentenceListSerializer
