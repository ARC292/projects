from django import forms
from .models import AwarenessCarousel

class AwarenessCarouselForm(forms.ModelForm):
    class Meta:
        model = AwarenessCarousel
        fields = ['image1', 'image2', 'image3', 'image4']
