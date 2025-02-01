from django.db import models
from django_quill.fields import QuillField
from django.utils.text import slugify
import html
from django.utils.html import strip_tags


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = QuillField()  # Valid default JSON for QuillField
    image = models.ImageField(upload_to='events/')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            this = Event.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass  # New object, no previous image to delete

        self.slug = slugify(self.title)
        if self.description:
            plain_text_content = html.unescape(strip_tags(str(self.description.html)))
            self.short_description = plain_text_content[:150]

        super().save(*args, **kwargs)  # Ensure the save method actually persists changes

    def __str__(self):
        return self.title
