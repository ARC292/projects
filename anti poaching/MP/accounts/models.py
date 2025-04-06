from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    position = models.CharField(
        max_length=6,
        choices=[('admin', 'Admin'), ('patrol', 'Patrol')],
        default='patrol'
    )
    region = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False  # Django won't touch the table
        db_table = 'users'  # Match your MySQL table name

    def __str__(self):
        return self.username
