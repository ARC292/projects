from django.contrib import admin
from .models import AwarenessCarousel

@admin.register(AwarenessCarousel)
class AwarenessCarouselAdmin(admin.ModelAdmin):
    list_display = ('id', 'image1', 'image2', 'image3', 'image4', 'updated_at')
    readonly_fields = ('updated_at',)
