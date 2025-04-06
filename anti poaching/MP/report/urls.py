
from django.urls import path
from . import views

urlpatterns = [
     path("", views.report, name='report'),
     path('report-success/<int:report_id>/', views.report_success, name='report_success'),
     path('check-status/', views.check_report_status, name='check_status'),
     path('submit-report/', views.submit_patrol_report, name='submit_patrol_report'),
    path('preport-success/', views.preport_success, name='preport_success'), 
    
     


]
