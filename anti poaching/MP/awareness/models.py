from django.db import models

class AwarenessCarousel(models.Model):
    image1 = models.ImageField(upload_to='carousel_images/')
    image2 = models.ImageField(upload_to='carousel_images/')
    image3 = models.ImageField(upload_to='carousel_images/')
    image4 = models.ImageField(upload_to='carousel_images/')
    updated_at = models.DateTimeField(auto_now=True)  # Track last update
