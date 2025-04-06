from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import login_view, admin_dashboard, patrol_dashboard, assign_patrol, resolve_report, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
  
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('patrol_dashboard/', patrol_dashboard, name='patrol_dashboard'),
    path('assign_patrol/', assign_patrol, name='assign_patrol'),
    path('resolve_report/<int:report_id>/', resolve_report, name='resolve_report'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
