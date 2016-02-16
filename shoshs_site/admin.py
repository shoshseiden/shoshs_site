from django.contrib import admin
from .models import Website, Graphic

admin.site.register(
    Website, list_display=["website_url", "website_name"]
)

admin.site.register(
    Graphic, list_display=["graphic_image", "graphic_image_description"]
)
