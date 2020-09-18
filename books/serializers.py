from rest_framework import serializers
from .models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'author', 'body', 'isbn', 'created_at')
        model = Books