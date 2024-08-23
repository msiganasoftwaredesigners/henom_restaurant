from django.db import models
from django.utils.text import slugify
from django.db.models import Q
from django.utils import timezone 

class MenuCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class MenuGroup(models.Model):
    name = models.CharField(max_length=255)
    menu_type = models.ForeignKey(MenuCategory, related_name='groups', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, blank=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('menu_type', 'slug')
        constraints = [
            models.UniqueConstraint(
                fields=['menu_type', 'slug'],
                name='unique_menu_group_per_type'
            )
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

class MenuItem(models.Model):
    menu_type = models.ForeignKey(MenuCategory, related_name='items', on_delete=models.CASCADE)
    menu_group = models.ForeignKey(MenuGroup, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2 , blank=True, null=True)

    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
