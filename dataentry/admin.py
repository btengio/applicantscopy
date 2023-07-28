from django.contrib import admin
from .models import MainApplicant, Spouse, Children

# Register your models here.
admin.site.register(Spouse)
admin.site.register(Children)

@admin.register(MainApplicant)
class MainApplicantAdmin(admin.ModelAdmin):
    list_display = MainApplicant.DisplayFields
    search_fields = MainApplicant.SearchableFields
    # list_filter = MainApplicant.FilterFields