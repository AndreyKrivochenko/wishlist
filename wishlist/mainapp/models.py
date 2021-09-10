from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """ Таблица "Товар"

    id
    Название товара
    Ссылка на товар
    Цена товара
    Дата и время создания записи
    Дата и время обновления записи
    """
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class WishList(models.Model):
    """ Таблица "Лист хотелок"

    id - Created Django
    owner - 
    products - ManyToMany
    is_hidden - bool
    """
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    products = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
