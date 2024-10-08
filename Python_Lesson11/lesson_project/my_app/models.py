from django.db import models

# Create your models here.

class BBoard(models.Model):
    title = models.CharField(max_length=50, verbose_name="название рекламы")
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"
        ordering = ['-published']

    def __str__(self):
        return self.title