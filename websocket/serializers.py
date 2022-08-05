
from rest_framework import serializers
from .models import Messages

class MessageSerializer(serializers.ModelSerializer):
    sent_to = serializers.StringRelatedField(source="to", many=False, read_only=True)
    sent_from = serializers.StringRelatedField(source="by", many=False, read_only=True)

    class Meta:
        model = Messages
        fields = ['id', 'to', 'title', 'message', 'by', 'created', 'sent_to', 'sent_from']
    