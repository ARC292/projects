from django.contrib import admin
from .models import PoachingReport, PatrolPoachingReport

@admin.register(PoachingReport)
class PoachingReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'date_time', 'type_of_poaching', 'status', 'ap')
    search_fields = ('location', 'type_of_poaching', 'ap')
    list_filter = ('status', 'type_of_poaching')

@admin.register(PatrolPoachingReport)
class PatrolPoachingReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'patrol_id', 'date_time', 'location', 'type_of_poaching')  # Removed 'status'
    search_fields = ('location', 'type_of_poaching')
    list_filter = ('date_time',)  # Removed 'status'
