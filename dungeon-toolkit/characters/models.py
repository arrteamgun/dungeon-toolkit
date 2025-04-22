from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Character(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Time Create')
    created_by = models.ForeignKey(get_user_model(),
                                   on_delete=models.SET_NULL,
                                   default=None, null=True, related_name='chars')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='Slug',
                            default=name,
                            validators=[
                                MinLengthValidator(
                                    limit_value=5, message=f'Too short, 5 symbols is minimum'),
                                MaxLengthValidator(
                                    100, message='Too long, 100 symbols is maximum')
                            ])

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]
