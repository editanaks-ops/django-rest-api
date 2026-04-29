#  Django REST API (Books & Categories)

Учебный проект на Django REST Framework.

##  Функционал

- CRUD для книг 
- CRUD для категорий 
- Swagger документация
- Админка Django

##  Технологии

- Python
- Django
- Django REST Framework
- drf-spectacular

##  Эндпоинты

### Books
- GET /api/books/
- POST /api/books/
- GET /api/books/{id}/
- PUT /api/books/{id}/
- DELETE /api/books/{id}/

### Categories
- GET /api/categories/
- POST /api/categories/
- GET /api/categories/{id}/
- PUT /api/categories/{id}/
- DELETE /api/categories/{id}/

##  Пример категорий

- Фантастика
- Детектив
- Роман

##  Документация

Swagger UI:  
http://127.0.0.1:8000/api/docs/

---

## Уровни реализации

### LITE
- Созданы модели Book и Category
- Реализован CRUD для книг и категорий
- Настроены базовые API endpoints

### PRO
- Добавлена связь Book → Category (ForeignKey)
- Реализован вложенный вывод книг внутри категории
- Использованы вложенные сериализаторы
- Добавлен отдельный endpoint для получения категории с книгами

---

## Эндпоинты

### Books
- GET /api/books/
- POST /api/books/
- GET /api/books/<id>/
- PUT /api/books/<id>/
- DELETE /api/books/<id>/

### Categories
- GET /api/categories/
- POST /api/categories/
- GET /api/categories/<id>/

### PRO (вложенные данные)
- GET /api/categories/<id>/detail/

---

## Технологии

- Python
- Django
- Django REST Framework
