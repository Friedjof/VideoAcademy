from django.db import models
from django.contrib import admin


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/course/images/')

    def __str__(self):
        return f"{self.title}"


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')
    course = models.ForeignKey(Course.__name__, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
