from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.TextField()
    location = models.TextField()
    date = models.DateTimeField()
    image_url = models.URLField(blank=True, null=True)
    def __str__(self):
        return f"Подія в {self.location}. Дата: {self.date}"
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["date"]
