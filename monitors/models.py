from django.db import models


class Monitor(models.Model):
    ip_address = models.GenericIPAddressField()
    slug = models.SlugField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)
    last_viewed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return ip_address

class Result(models.Model):
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
