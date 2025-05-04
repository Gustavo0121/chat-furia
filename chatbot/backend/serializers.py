"""Serializer."""

from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    """MessageSerializer."""

    class Meta:
        """Meta."""

        model = Message
        fields = ['id', 'content', 'sender', 'timestamp']
