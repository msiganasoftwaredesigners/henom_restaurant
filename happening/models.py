from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='events/')
    event_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
