from django.db import models
from django.conf import settings

class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Media(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='portfolio_media/')

    def __str__(self):
        return f"Media for {self.portfolio.title}"
