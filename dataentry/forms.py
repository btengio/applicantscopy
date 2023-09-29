from django.forms.models import inlineformset_factory
from .models import Applicant, Dependant

ApplicantDependantFormset = inlineformset_factory(Applicant, Dependant, fields='__all__', extra=6)