from django.core.management.base import BaseCommand

from app_work.models import Specialty, Company, Vacancy
from data import specialties, jobs, companies


class Command(BaseCommand):

    def handle(self, *args, **options):

        for specialty in specialties:
            if Specialty.objects.filter(code=specialty['code']).count() == 0:
                Specialty.objects.create(code=specialty['code'], title=specialty['title'])
            else:
                continue

        for company in companies:
            if Company.objects.filter(name=company['title']).count() == 0:
                Company.objects.create(
                    name=company['title'],
                    location=company['location'],
                    description=company['description'],
                    employee_count=int(company['employee_count']),
                )
            else:
                continue

        for job in jobs:
            if Vacancy.objects.filter(pk=int(job['id'])).count() == 0:
                Vacancy.objects.create(
                    title=job['title'],
                    specialty=Specialty.objects.get(code=job['specialty']),
                    company=Company.objects.get(pk=int(job['company'])),
                    skills=job['skills'],
                    description=job['description'],
                    salary_min=job['salary_from'],
                    salary_max=job['salary_to'],
                    published_at=job['posted']
                )

