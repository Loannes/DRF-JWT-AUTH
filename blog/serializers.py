from .models import Post
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'body', 'created_at']