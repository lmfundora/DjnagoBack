from django.db import models

# Create your models here.
class LabelsModel(models.Model):
    label = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.label

class PelisModel(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    release_date = models.DateField()
    director = models.CharField(max_length=200)
    labels = models.ManyToManyField(LabelsModel)
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()
    posted_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


