from rest_framework import serializers
from django.utils import timezone
from .models import *

# Serializer for nested author representation
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['username', 'name', 'contact']

# Main Book serializer with all core features
class BookSerializer(serializers.ModelSerializer):
    # Input/output foreign key using slug field instead of ID
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=Author.objects.all()
    )
    # Read-only computed field
    is_recent = serializers.SerializerMethodField()
    # Write-only input field, won't be included in response
    secret_note = serializers.CharField(write_only=True)
    # Read-only field included in output only
    id = serializers.IntegerField(read_only=True)

    # Add dynamic/computed field for recent publication
    def get_is_recent(self, obj):
        return obj.created_at.year == timezone.now().year

    # Field-level validation: validate title
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title too short")
        return value

    # Object-level validation (all fields together)
    def validate(self, data):
        if data.get('published') and "draft" in data.get('title', '').lower():
            raise serializers.ValidationError("Drafts can't be published")
        return data

    # Called during serializer.save() on POST
    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    # Called during serializer.save(instance=...) on PUT/PATCH
    def update(self, instance, validated_data):
        # Keep existing value if not provided
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.published = validated_data.get('published', instance.published)
        instance.secret_note = validated_data.get('secret_note', instance.secret_note)
        instance.save()
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['title'] = f"📘 {instance.title.upper()}"
        return rep

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published', 'secret_note', 'is_recent']

# Serializer for creating a book with new author at the same time
class BookNestedCreateSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nested input instead of SlugRelatedField

    class Meta:
        model = Book
        fields = ['title', 'author', 'published', 'secret_note']

    def create(self, validated_data):
        # Extract nested data for author
        author_data = validated_data.pop('author')
        author = Author.objects.create(**author_data)
        return Book.objects.create(author=author, **validated_data)

# Optional dynamic version of BookSerializer that allows filtering fields
class DynamicBookSerializer(BookSerializer):
    def __init__(self, *args, **kwargs):
        # Pull specific field list from kwargs before super init
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)
        # Drop unrequested fields if specified
        if fields:
            allowed = set(fields)
            for field in set(self.fields) - allowed:
                self.fields.pop(field)
