from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.TextField()
    location = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    def __str__(self):
        return f"Подія в {self.location}. Дата: {self.date}"
    class Meta:
        verbose_name = "Events"
        ordering = ["date"]
