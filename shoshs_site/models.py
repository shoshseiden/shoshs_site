from django.db import models


class Website(models.Model):
    website_name = models.CharField(max_length=25)
    website_url = models.CharField(max_length=100)
    website_screenshot = models.ImageField(upload_to="website_images")

    def __str__(self):
        return self.website_name


class Graphic(models.Model):
    graphic_image = models.ImageField(upload_to="graphic_images")
    graphic_image_description = models.CharField(max_length=100)

    def __str__(self):
        return self.graphic_image_description
