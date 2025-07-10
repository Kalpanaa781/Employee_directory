from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.job_title}"
