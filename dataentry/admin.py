from django.contrib import admin
from .models import Applicant, Dependant

# Register your models here.

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = Applicant.DisplayFields
    search_fields = Applicant.SearchableFields
    # list_filter = MainApplicant.FilterFields

@admin.register(Dependant)
class DependantAdmin(admin.ModelAdmin):
    list_display = Dependant.DisplayFields
    search_fields = Dependant.SearchableFields
    # list_filter = MainApplicant.FilterFields