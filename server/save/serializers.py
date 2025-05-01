from rest_framework import serializers
from .models import Save

class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = ['id', 'user', 'link', 'caption', 'image', 'tag', 'saved_at']
        read_only_fields = ['user']