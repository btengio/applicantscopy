from django.shortcuts import render, redirect
from .models import MainApplicant, Children, Spouse

# Create your views here.
def homepage(request):
    return render(request, 'base.html')

def dataentry(request):
    if request.method == 'POST':
        if request.POST.get('application_number') and request.POST.get('region') and request.POST.get('family_name') and request.POST.get('first_name') and request.POST.get('middle_name') and request.POST.get('gender') and request.POST.get('month_B') and request.POST.get('day_B') and request.POST.get('year_B') and request.POST.get('birth_city') and request.POST.get('birth_country') and request.POST.get('eligibility_country') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('highest_education') and request.POST.get('no_of_children') and request.POST.get('marital_status'):
            applicant = MainApplicant()
            applicant.application_number = request.POST.get('application_number')
            applicant.region = request.POST.get('region')
            applicant.family_name = request.POST.get('family_name')
            applicant.first_name = request.POST.get('first_name')
            applicant.middle_name = request.POST.get('middle_name')
            applicant.gender = request.POST.get('gender')
            applicant.month_B = request.POST.get('month_B')
            applicant.day_B = request.POST.get('day_B')
            applicant.year_B = request.POST.get('year_B')
            applicant.birth_city = request.POST.get('birth_city')
            applicant.birth_country = request.POST.get('birth_country')
            applicant.eligibility_country = request.POST.get('eligibility_country')
            applicant.phone = request.POST.get('phone')
            applicant.email = request.POST.get('email')
            applicant.highest_education = request.POST.get('highest_education')
            applicant.no_of_children = int(request.POST.get('no_of_children'))
            if applicant.no_of_children >= 1:
                if request.POST.get('dress_color') and request.POST.get('family_name') and request.POST.get('first_name') and request.POST.get('middle_name') and request.POST.get('gender') and request.POST.get('month_B') and request.POST.get('day_B') and request.POST.get('year_B') and request.POST.get('birth_city') and request.POST.get('birth_country'):
                    child = Children()
                    child.main_applicant = applicant.id #am failing to reference this FK in forms!!
                    child.dress_color = request.POST.get('dress_color')
                    child.family_name = request.POST.get('family_name')
                    child.first_name = request.POST.get('first_name')
                    child.middle_name = request.POST.get('middle_name')
                    child.gender = request.POST.get('gender')
                    child.month_B = request.POST.get('month_B')
                    child.day_B = request.POST.get('day_B')
                    child.year_B = request.POST.get('year_B')
                    child.birth_city = request.POST.get('birth_city')
                    child.birth_country = request.POST.get('birth_country')

            applicant.marital_status = request.POST.get('marital_status')
            if applicant.marital_status == 'Marred':
                if request.POST.get('family_name') and request.POST.get('first_name') and request.POST.get('middle_name') and request.POST.get('gender') and request.POST.get('month_B') and request.POST.get('day_B') and request.POST.get('year_B') and request.POST.get('birth_city') and request.POST.get('birth_country'):
                    spouse = Spouse()
                    spouse.main_applicant = applicant.id #am failing to reference this FK in forms!!
                    spouse.family_name = request.POST.get('family_name')
                    spouse.first_name = request.POST.get('first_name')
                    spouse.middle_name = request.POST.get('middle_name')
                    spouse.gender = request.POST.get('gender')
                    spouse.month_B = request.POST.get('month_B')
                    spouse.day_B = request.POST.get('day_B')
                    spouse.year_B = request.POST.get('year_B')
                    spouse.birth_city = request.POST.get('birth_city')
                    spouse.birth_country = request.POST.get('birth_country')

            child.save()
            spouse.save()
            applicant.save()

            return render(request, 'dataentry.html')
    else:
        return render(request, 'dataentry.html')



def applicants(request):
    all_applicants = MainApplicant.objects.all()
    return render(request, 'applicants.html', {'all_applicants':all_applicants})

def update_applicants(request, id):
    applicant = MainApplicant.objects.get(id=id)
    return render(request, 'update_applicant.html', {'applicant': applicant})

# Delete applicant
def delete_applicants(request, id):
    applicant = MainApplicant.objects.get(id=id)
    applicant.delete()
    return redirect('applicants')

def login(request):
    return render(request, 'loginpage.html')

def contact(request):
    return render(request, 'contact.html')
