from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
MARITAL_CHOICES = (
        ('single','SINGLE'),
        ('married','MARRIED'),
        ('divorced','DIVORCED'),
    )

GENDER_CHOICES = (
        ('male','MALE'),
        ('female','FEMALE'),
    )

REGION_CHOICES = (
        ('ar','ARUSHA'),
        ('dar','DAR'),
        ('dom','DODOMA'),
        ('kgm','KIGOMA'),
        ('klm','KILIMANJARO'),
        ('mby','MBEYA'),
        ('mza','MWANZA'),
        ('kny','KENYA'),
        ('online','ONLINE'),
        ('znz','ZANZIBAR'),
    )

MONTH_CHOICES = (
        ('1','JANUARY'),
        ('2','FEBRUARY'),
        ('3','MARCH'),
        ('4','APRIL'),
        ('5','MAY'),
        ('6','JUNE'),
        ('7','JULY'),
        ('8','AUGUST'),
        ('9','SEPTEMBER'),
        ('10','OCTOBER'),
        ('11','NOVEMBER'),
        ('12','DECEMBER'),
    )

EDUCATION_CHOICES = (
    ('PR','PRIMARY SCH'),
    ('HSND','HIGH SCH NO DGR'),
    ('HSD','HIGH SCH DGR'),
    ('VS','VOCATIONAL SCH'),
    ('UC','SOME UNIVERSITY COURSES'),
    ('UD','UNIVERSITY DEGREE'),
    ('GRC','SOME GRADUATE LEVEL COURSES'),
    ('MSC','MASTERS'),
    ('DOC','SOME DOCTORATE LEVEL COURSES'),
    ('PHD','DOCTORATE DEGREE'),
)
    
# Main applicant starts here
class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #task to stay models.SET_NULL
    application_number = models.CharField(null=False, blank=False, unique=True, max_length=255)
    region = models.CharField(max_length=20, choices=REGION_CHOICES)
    family_name = models.CharField(null=False, blank=False, max_length=255)
    first_name = models.CharField(null=False, blank=False, max_length=255)
    middle_name = models.CharField(blank=True, max_length=255)
    gender = models.CharField(max_length=10, null=False, choices=GENDER_CHOICES)
    month_B = models.CharField(null=False, choices=MONTH_CHOICES, max_length=100)
    day_B = models.PositiveIntegerField(blank=False, null=False)
    year_B = models.PositiveIntegerField(blank=False, null=False)
    birth_city = models.CharField(max_length=255, null=False)
    birth_country = models.CharField(max_length=255, null=False)
    eligibility_country = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, unique=False)
    highest_education = models.CharField(max_length=255, null=False, choices=EDUCATION_CHOICES)
    no_of_children = models.PositiveIntegerField(null=False)
    marital_status = models.CharField(max_length=255, null=False, choices=MARITAL_CHOICES)
    DisplayFields = ['id','application_number','region','family_name','first_name','middle_name','gender','month_B','day_B','year_B','birth_city','birth_country','eligibility_country','phone','email','highest_education','no_of_children','marital_status']
    SearchableFields = ['family_name','first_name']
    FilterFields = ['region']

    def get_absolute_url(self):
        return reverse('dataentry:applicant_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.family_name
    
    class Meta:
        ordering = ('family_name',)
        verbose_name_plural = 'Applicants'
    

# Dependant details goes here
class Dependant(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #task to stay models.SET_NULL
    main_applicant = models.ForeignKey('Applicant', blank=False, null=False, on_delete=models.CASCADE,related_name='applicant_dependant')
    family_name = models.CharField(null=False, blank=False, max_length=255)
    first_name = models.CharField(null=False, blank=False, max_length=255)
    middle_name = models.CharField(blank=True, max_length=255)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    month_B = models.CharField(blank=False, choices=MONTH_CHOICES, max_length=100)
    day_B = models.PositiveIntegerField(blank=False)
    year_B = models.PositiveIntegerField(blank=False)
    birth_city = models.CharField(max_length=255)
    birth_country = models.CharField(max_length=255)
    dress_or_shirt_color = models.CharField(blank=True, max_length=50)
    DisplayFields = ['id','family_name','first_name','middle_name','gender','month_B','day_B','year_B','birth_city','birth_country']
    SearchableFields = ['family_name','first_name']
    FilterFields = ['main_applicant']


    def __str__(self):
        return self.main_applicant.family_name
    
    class Meta:
        ordering = ('family_name',)
        verbose_name_plural = 'Dependants'


