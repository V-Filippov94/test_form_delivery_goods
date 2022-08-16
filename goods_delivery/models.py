from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    type = models.CharField(max_length=255, verbose_name='Тип товара')
    date_delivery = models.DateField(verbose_name='Дата доставки')
    file = models.FileField(upload_to='goods_delivery/files', verbose_name='Файл', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявка'


class AddressIssuance(models.Model):
    address = models.TextField(verbose_name='Пункт выдачи')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адрес'
