from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *

class PostSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=True)
    
    class Meta:
        model = Post
        fields = '__all__'
    
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'