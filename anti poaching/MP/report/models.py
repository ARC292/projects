from django.db import models

class PoachingReport(models.Model):
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    
    POACHING_TYPES = [
        ('Hunting', 'Hunting'),
        ('Illegal Fishing', 'Illegal Fishing'),
        ('Traps', 'Traps'),
    ]
    type_of_poaching = models.CharField(max_length=50, choices=POACHING_TYPES)
    
    methods_used = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    num_people = models.IntegerField(blank=True, null=True)
    vehicles_boats = models.CharField(max_length=255, blank=True, null=True)
    evidence = models.FileField(upload_to='evidence/', blank=True, null=True)
    
    
    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Assigned', 'Assigned'),
        ('Resolved', 'Resolved'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Submitted')
    ap = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"Report at {self.location} on {self.date_time} (Status: {self.status})"
    
    
class PatrolPoachingReport(models.Model):
    patrol_id = models.CharField(max_length=255)  # Stores the patrol ID
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)

    POACHING_TYPES = [
        ('Hunting', 'Hunting'),
        ('Illegal Fishing', 'Illegal Fishing'),
        ('Traps', 'Traps'),
    ]
    type_of_poaching = models.CharField(max_length=50, choices=POACHING_TYPES)

    methods_used = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    num_people = models.IntegerField(blank=True, null=True)
    vehicles_boats = models.CharField(max_length=255, blank=True, null=True)
    evidence = models.FileField(upload_to='evidence/', blank=True, null=True)

    def __str__(self):
        return f"Patrol {self.patrol_id} report at {self.location} on {self.date_time}"

    

# After adding this model, run:
# python manage.py makemigrations
# python manage.py migrate

# This way, reports start as 'Submitted', and the admin can assign them to a patrol (ap field) later!
