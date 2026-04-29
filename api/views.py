from rest_framework.generics import ListCreateAPIView
from .models import Book
from .serializers import BookSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Category
from .serializers import CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
@extend_schema(
    summary="Получение списка книг",
    description="Этот эндпоинт позволяет получить список всех книг в базе данных. "
                "Вы также можете добавить новую книгу с помощью POST-запроса.",
    responses={200: BookSerializer(many=True)}
)
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@extend_schema(
    summary="Работа с конкретной книгой",
    description="Позволяет получить информацию о книге, обновить её данные или удалить.",
    responses={
        200: BookSerializer,
        204: None
    }
)
class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Представление для работы с отдельной книгой: просмотр, обновление и удаление.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer