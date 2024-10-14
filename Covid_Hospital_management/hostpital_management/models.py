from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name

class Bed(models.Model):
    bed_number = models.CharField(max_length=10)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Bed {self.bed_number}"

class Patient(models.Model):
    STATUS_CHOICES = [
        ('Admitted', 'Admitted'),
        ('Recovered', 'Recovered'),
        ('Deceased', 'Deceased'),
    ]

    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=15)
    patient_relative_name = models.CharField(max_length=100, blank=True, null=True)
    patient_relative_contact = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255)
    symptoms = models.TextField()
    prior_ailments = models.TextField(blank=True, null=True)
    bed_num = models.ForeignKey(Bed, on_delete=models.SET_NULL, null=True, blank=True)
    dob = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Admitted')
    doctors_visiting_time = models.TimeField(blank=True, null=True)
    doctors_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
