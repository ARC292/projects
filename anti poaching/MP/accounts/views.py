from django.conf import settings
from django.shortcuts import render, redirect
from django.db import connection
from .forms import LoginForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.cache import never_cache
from django.utils.decorators import decorator_from_middleware
from django.middleware.cache import CacheMiddleware


def login_view(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            with connection.cursor() as cursor:
                cursor.execute("SELECT position FROM users WHERE username=%s AND password=%s", [username, password])
                user = cursor.fetchone()

            if user:
                position = user[0]
                
                # Store user info in session
                request.session['username'] = username
                request.session['position'] = position
                request.session.set_expiry(1800)  # Auto logout after 30 min
                
                if position == 'admin':
                    return redirect('admin_dashboard')
                elif position == 'patrol':
                    return redirect('patrol_dashboard')
            else:
                error = "Invalid Username or Password"

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form, 'error': error})




def logout_view(request) -> HttpResponseRedirect:
    request.session.flush()  # Clear session
    return redirect('login')  # Redirect to login page





@never_cache
def admin_dashboard(request):
    if not request.session.get('username') or request.session.get('position') != 'admin':
        messages.error(request, "Unauthorized access!")
        return redirect('login')

    submitted_reports, assigned_reports, resolved_reports, patrol_reports = [], [], [], []

    with connection.cursor() as cursor:
        # Fetch submitted reports
        cursor.execute("""
            SELECT id, date_time, location, type_of_poaching, methods_used, duration, 
                   num_people, vehicles_boats, evidence, status, ap 
            FROM report_poachingreport 
            WHERE status = 'submitted' 
            ORDER BY date_time DESC
        """)
        submitted_reports = cursor.fetchall()

        # Fetch patrol users grouped by region
        patrol_users_by_location = {}
        cursor.execute("SELECT username, region FROM users WHERE position = 'patrol'")
        patrols = cursor.fetchall()
        
        for patrol in patrols:
            username, region = patrol
            patrol_users_by_location.setdefault(region, []).append(username)

        # Fetch assigned reports
        cursor.execute("""
            SELECT id, date_time, location, type_of_poaching, methods_used, duration, 
                   num_people, vehicles_boats, evidence, status, ap 
            FROM report_poachingreport 
            WHERE status = 'assigned' 
            ORDER BY date_time DESC
        """)
        assigned_reports = cursor.fetchall()

        # Fetch resolved reports
        cursor.execute("""
            SELECT id, date_time, location, type_of_poaching, methods_used, duration, 
                   num_people, vehicles_boats, evidence, status, ap 
            FROM report_poachingreport 
            WHERE status = 'resolved' 
            ORDER BY date_time DESC
        """)
        resolved_reports = cursor.fetchall()

        # ✅ Fetch patrol reports
        cursor.execute("""
            SELECT id, patrol_id, date_time, location, type_of_poaching, methods_used, 
                   num_people, vehicles_boats, evidence
            FROM report_patrolpoachingreport 
            ORDER BY date_time DESC
        """)
        patrol_reports = cursor.fetchall()

    return render(request, 'accounts/admin_dashboard.html', {
        'submitted_reports': submitted_reports,
        'assigned_reports': assigned_reports,
        'resolved_reports': resolved_reports,
        'patrol_users_by_location': patrol_users_by_location,
        'patrol_reports': patrol_reports,  # ✅ Add patrol reports to context
        'MEDIA_URL': settings.MEDIA_URL,
    })


@never_cache
def patrol_dashboard(request):
    if not request.session.get('username') or request.session.get('position') != 'patrol':
        messages.error(request, "Unauthorized access!")
        return redirect('login')

    patrol_username = request.session.get('username')
    assigned_reports = []

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, date_time, location, type_of_poaching, methods_used, duration, 
                   num_people, vehicles_boats, evidence, status 
            FROM report_poachingreport 
            WHERE ap = %s AND status = 'assigned'
            ORDER BY date_time DESC
        """, [patrol_username])
        assigned_reports = cursor.fetchall()

    return render(request, 'accounts/patrol_dashboard.html', {
        'assigned_reports': assigned_reports,
        'MEDIA_URL': settings.MEDIA_URL,
    })


def assign_patrol(request):
    if request.session.get('position') != 'admin':
        return redirect('login')

    if request.method == 'POST':
        report_id = request.POST.get('report_id')
        patrol_username = request.POST.get('patrol_username')

        if report_id and patrol_username:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE report_poachingreport 
                    SET ap = %s, status = 'assigned' 
                    WHERE id = %s
                """, [patrol_username, report_id])

        return redirect('admin_dashboard')




def resolve_report(request, report_id):
    if not request.session.get('username') or request.session.get('position') != 'patrol':
        messages.error(request, "Unauthorized access!")
        return redirect('login')

    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE report_poachingreport 
                SET status = 'resolved' 
                WHERE id = %s
            """, [report_id])

        return redirect('patrol_dashboard')
