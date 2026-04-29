from rest_framework import serializers
from .models import Book, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )

    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'title': {'help_text': 'Название книги'},
            'author': {'help_text': 'Автор книги'},
            'published_date': {'help_text': 'Дата публикации (формат YYYY-MM-DD)'},
            'isbn': {'help_text': 'Уникальный ISBN номер книги'},
            'page_count': {'help_text': 'Количество страниц'},
            'cover': {'help_text': 'Ссылка на изображение обложки'},
        }


class CategoryDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'books']
