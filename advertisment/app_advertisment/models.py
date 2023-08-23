from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/', null=True, blank=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S:')
            return format_html(
                '<span style="color: green; font-weight: bold">Сегодня в {} </span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y. в %H:%M:%S:')
    
    @admin.display(description='Дата последнего обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S:')
            return format_html(
                '<span style="color: blue; font-weight: bold">Сегодня в {} </span>', updated_time
            )
        return self.updated_at.strftime('%d.%m.%Y. в %H:%M:%S:')
    
    @admin.display(description='Изображение в админке')
    def image_display(self):
        if self.image:
            return format_html(
                '<img src= "{}" style="max-width: 100px; max-height:100px;" />', self.image.url
            )
        
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements" 