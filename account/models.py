from django.db import models
class Profile(models.Model):
    GENDER_CHOICES = [
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    ]
    
    name = models.CharField(max_length=100, verbose_name= 'Имя')
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(verbose_name= 'Описание')
    image = models.ImageField(upload_to='posts_img', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name
