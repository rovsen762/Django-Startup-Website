from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonial/%Y/%m/%d/')
    description = models.TextField()
    avaiable = models.BooleanField(default=True)

    def __str__(self):
        return self.name