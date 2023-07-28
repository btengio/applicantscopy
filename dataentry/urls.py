from django.urls import path
from. import views

urlpatterns = [
    path('', views.homepage, name="index"),
    path('contact/', views.contact, name='contact'),
    path('dataentry/', views.dataentry, name='dataentry'),
    path('applicants/', views.applicants, name='applicants'),
    path('update_applicants/<int:id>', views.update_applicants, name='update_applicants'),
    path('delete_applicants/<int:id>', views.delete_applicants, name='delete_applicants'),
    path('login/', views.login, name='login'),
]