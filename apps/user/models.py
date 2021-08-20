from django.db import models
from django.contrib.auth.models import User


class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country_of_news = models.TextField(null=True, blank=True)
    news_source = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
