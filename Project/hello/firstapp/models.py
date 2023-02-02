from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name="Категория:",
        max_length=100,
        unique=True)
    desc = models.TextField(verbose_name="Описание:")
    CATEGORIES = (
        (1, "Электроника:"),
        (2, "Одежда:"),
        (3, "Гаджеты:"),
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="", max_length=200)
    desc = models.TextField(verbose_name="")
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name="Цена:")
    pub_date = models.DateTimeField(verbose_name="Дата публикации:")
    in_stock = models.BooleanField(
        default=True,
        db_index=True,
        verbose_name="В наличии:")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    class Meta:
        ordering = ["-price", "name"]
        unique_together = [
            "category",
            "name",
            "price",
        ]
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + "( Нет в наличии )"
        return s

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Product, self).delete(*args, **kwargs)


