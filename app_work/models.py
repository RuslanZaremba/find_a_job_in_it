from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=50)
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField(default=0)
    salary_max = models.IntegerField(default=0)
    published_at = models.DateField()

    def __str__(self):
        return f"{self.title}"


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Specialty(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    picture = models.URLField(default='https://place-hold.it/100x60')

    def __str__(self):
        return f"{self.code}"
