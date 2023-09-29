from django.urls import path
from .views import ApplicantList, ApplicantDetail, ApplicantCreate, ApplicantUpdate, ApplicantDelete, ApplicantDependantUpdate, PdfDetail, UserLogin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', ApplicantList.as_view(), name='applicants'),
    path('applicant/<int:pk>/', ApplicantDetail.as_view(), name='applicant'),
    path('applicant/<int:pk>/pdf/', PdfDetail.as_view(), name='applicant-pdf-detail'),
    path('applicant-create/', ApplicantCreate.as_view(), name='applicant-create'),
    path('applicant-update/<int:pk>/', ApplicantUpdate.as_view(), name='applicant-update'),
    path('applicant-dependant-update/<int:pk>/', ApplicantDependantUpdate.as_view(), name='applicant-dependant-update'),
    path('applicant-delete/<int:pk>/', ApplicantDelete.as_view(), name='applicant-delete'),
]