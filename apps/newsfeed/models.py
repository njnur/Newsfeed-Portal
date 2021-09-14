from django.db import models


class News(models.Model):
    headline = models.TextField(null=True, blank=True, unique=True)
    thumbnail = models.URLField(null=True, blank=True)
    source = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    news_link = models.URLField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.headline[: 10]
