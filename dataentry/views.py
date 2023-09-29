from django.forms.forms import BaseForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from .models import Applicant, Dependant
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .forms import ApplicantDependantFormset
from easy_pdf.views import PDFTemplateResponseMixin


# Create your views here.
class UserLogin(LoginView):
    template_name = 'dataentry/login.html'
    fields  = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('applicants')
    
class ApplicantList(LoginRequiredMixin, ListView):
    model = Applicant
    context_object_name = 'applicants'
    # paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['applicants'] = context['applicants'].filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['applicants'] = context['applicants'].filter(family_name__startswith=search_input)
        context['search_input'] = search_input

        return context

class ApplicantDetail(LoginRequiredMixin, DetailView):
    model = Applicant
    context_object_name = 'applicant'
    # template_name = 'dataentry/applicant.html'

class PdfDetail(LoginRequiredMixin, PDFTemplateResponseMixin, DetailView):
    model = Applicant
    context_object_name = 'applicant'
    template_name = 'dataentry/pdf_detail.html'

class ApplicantCreate(LoginRequiredMixin, CreateView):
    model = Applicant
    fields = '__all__'
    success_url = reverse_lazy('applicants')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ApplicantCreate, self).form_valid(form)

class ApplicantUpdate(LoginRequiredMixin, UpdateView):
    model = Applicant
    fields = '__all__'
    success_url = reverse_lazy('applicants')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ApplicantUpdate, self).form_valid(form)

class ApplicantDelete(LoginRequiredMixin, DeleteView):
    model = Applicant
    context_object_name = 'applicant'
    success_url = reverse_lazy('applicants')

class ApplicantDependantUpdate(LoginRequiredMixin, SingleObjectMixin, FormView):

    model = Applicant
    template_name = 'dataentry/applicant_dependant_update.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Applicant.objects.all())
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object(queryset=Applicant.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self, form_class = None):
        return ApplicantDependantFormset(**self.get_form_kwargs(), instance=self.object)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save(commit=False)

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved'
        )
        form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('applicant', kwargs={'pk': self.object.pk})
