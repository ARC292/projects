from django import forms
from .models import PoachingReport, PatrolPoachingReport

# **Form for General Poaching Reports**
class ReportForm(forms.ModelForm):
    class Meta:
        model = PoachingReport
        fields = "__all__"  # Includes all fields from the PoachingReport model

    date_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=True)


# **Form for Patrol Reports**
class PatrolReportForm(forms.ModelForm):
    class Meta:
        model = PatrolPoachingReport
        fields = '__all__'  # Includes all fields including patrol_id

    date_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=True)
