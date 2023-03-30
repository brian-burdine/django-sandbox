from django.db import models

# Create your models here.
class Ability(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "abilities"

class Relationship(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name
        
class Hero(models.Model):
    name = models.CharField(max_length=100)
    about_me = models.CharField(max_length=200)
    biography = models.TextField()
    abilities = models.ManyToManyField(Ability)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "heroes"
    
    def __str__(self):
        return self.name
