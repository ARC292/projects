from django.urls import path
from . import views

urlpatterns = [
    path('', views.awareness, name='awareness'),  # Match base /awareness/ path
    path('update-carousel/',views.update_carousel, name='update_carousel'),
]
