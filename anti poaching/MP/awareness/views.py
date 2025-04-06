from django.shortcuts import render, redirect
from .models import AwarenessCarousel
from .forms import AwarenessCarouselForm

def update_carousel(request):
    carousel = AwarenessCarousel.objects.first()  # Get the first record (only one carousel)

    if request.method == "POST":
        form = AwarenessCarouselForm(request.POST, request.FILES, instance=carousel)
        if form.is_valid():
            form.save()
            return redirect('update_carousel')  # Reload page after saving

    else:
        form = AwarenessCarouselForm(instance=carousel)

    return render(request, 'awareness/update_carousel.html', {'form': form})

def awareness(request):
    carousel = AwarenessCarousel.objects.first()  # Fetch the images
    return render(request, 'awareness/awareness_page.html', {'carousel': carousel})
