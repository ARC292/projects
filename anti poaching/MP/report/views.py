from .models import PoachingReport
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import PatrolPoachingReport
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatrolReportForm  # Import the form
from .models import PatrolPoachingReport  # Import your model
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def report(request):
    if request.method == "POST":
        # Capture form data
        date_time = request.POST.get("date_time")
        location = request.POST.get("location")
        type_of_poaching = request.POST.get("type_of_poaching")
        methods_used = request.POST.get("methods_used")
        duration = request.POST.get("duration")
        num_people = request.POST.get("num_people")
        vehicles_boats = request.POST.get("vehicles_boats")
        evidence = request.FILES.get("evidence")

        # Save to the database and capture the ID
        report_instance = PoachingReport.objects.create(
            date_time=date_time,
            location=location,
            type_of_poaching=type_of_poaching,
            methods_used=methods_used,
            duration=duration,
            num_people=num_people,
            vehicles_boats=vehicles_boats,
            evidence=evidence,
        )

        # Redirect to success page with the report ID
        return redirect('report_success', report_id=report_instance.id)

    return render(request, "report/report.html")






def report_success(request, report_id):
    report = get_object_or_404(PoachingReport, id=report_id)
    return render(request, 'report/success.html', {'report_id': report.id})

def check_report_status(request):
    report = None
    error_message = None

    if request.method == "POST":
        report_id = request.POST.get("report_id")
        
        try:
            # Fetch the report by ID
            report = PoachingReport.objects.get(id=report_id)
        except PoachingReport.DoesNotExist:
            error_message = "Report not found. Please check the ID and try again."

    return render(request, 'report/check_status.html', {'report': report, 'error_message': error_message})




def submit_patrol_report(request):
    if request.method == "POST":
        form = PatrolReportForm(request.POST, request.FILES)
        if form.is_valid():
            patrol_report = form.save(commit=False)  # Don't save yet
            patrol_report.save()  # Now save to DB
            return redirect('preport_success')  # Redirect to success page
    else:
        form = PatrolReportForm()
    
    return render(request, 'report/submit_report.html', {'form': form})


def preport_success(request):
    return render(request, 'report/psuccess.html')  # Renders the success template










