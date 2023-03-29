from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=100)
    about_me = models.CharField(max_length=200)
    biography = models.TextField()

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "heroes"

class AbilityType(models.Model):
    name = models.CharField(max_length=80)

class RelationshipType(models.Model):
    name = models.CharField(max_length=80)