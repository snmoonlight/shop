from django.db import models


class Orders(models.Model):
    otype = models.CharField('Вид продажи', default='', max_length=250, blank=True, null=True)
    odate = models.DateField('Дата продажи', max_length=250, default='', blank=True, null=True)
    onumb = models.CharField('Номер кассового аппарата', max_length=250, default='', blank=True, null=True)
    oname = models.CharField('Имя покупателя', max_length=250, default='', blank=True, null=True)
    oitems = models.CharField('Товары', max_length=250, default='', blank=True, null=True)
    osumm = models.CharField('Общая сумма', max_length=250, default='', blank=True, null=True)
    oreason = models.CharField('Причина возврата', max_length=250, default='', blank=True, null=True)
    ovozn = models.CharField('Номер документа продажи', max_length=250, default='', blank=True, null=True)
    ovozd = models.CharField('Дата документа продажи', max_length=250, default='', blank=True, null=True)

    def __str__(self):
        return self.otype

    def get_absolute_url(self):
        m = self.otype
        return '/jorn'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
