from rest_framework import serializers
from .models import Task, Tag, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'color']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.email', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'tags', 'category', 'owner']


class CommentSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ['id', 'task', 'comment', 'created_at']
