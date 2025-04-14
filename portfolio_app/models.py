from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(max_length=300)

    def __str__(self):
        return self.name
