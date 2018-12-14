from django.db import models


class Monitor(models.Model):
    ip_address = models.GenericIPAddressField()
    slug = models.SlugField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)
    last_viewed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.ip_address

    def save(self, *args, **kwargs):
        if not self.pk:
            # create a new slug if this is a new object
            self.slug = self.ip_address.replace(".", "-")

        super(Monitor, self).save(*args, **kwargs)

class Result(models.Model):
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_saved = models.BooleanField(default=False)
    latency = models.DecimalField(max_digits=10, decimal_places=3, default=0.000)
    packet_loss = models.IntegerField(default=0)

    def __str__(self):
        return str(self.date_created)
