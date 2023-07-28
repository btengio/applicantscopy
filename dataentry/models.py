from django.db import models

# Create your models here.
# MARITAL_CHOICES = (
#         ('single','SINGLE'),
#         ('married','MARRIED'),
#         ('divorced','DIVORCED'),
#     )

# GENDER_CHOICES = (
#         ('male','MALE'),
#         ('female','FEMALE'),
#     )

# REGION_CHOICES = (
#         ('ar','ARUSHA'),
#         ('dar','DAR'),
#         ('dom','DODOMA'),
#         ('kgm','KIGOMA'),
#         ('klm','KILIMANJARO'),
#         ('mby','MBEYA'),
#         ('mza','MWANZA'),
#         ('online','ONLINE'),
#         ('znz','ZANZIBAR'),
#     )

# MONTH_CHOICES = (
#         ('JAN','JANUARY'),
#         ('FEB','FEBRUARY'),
#         ('MAR','MARCH'),
#         ('APR','APRIL'),
#         ('MAY','MAY'),
#         ('JUN','JUNE'),
#         ('JUL','JULY'),
#         ('AUG','AUGUST'),
#         ('SEPT','SEPTEMBER'),
#         ('OCT','OCTOBER'),
#         ('NOV','NOVEMBER'),
#         ('DEC','DECEMBER'),
#     )

# EDUCATION_CHOICES = (
#     ('PR','PRIMARY SCH'),
#     ('HSND','HIGH SCH NO DGR'),
#     ('HSD','HIGH SCH DGR'),
#     ('VS','VOCATIONAL SCH'),
#     ('UC','SOME UNIVERSITY COURSES'),
#     ('UD','UNIVERSITY DEGREE'),
#     ('GRC','SOME GRADUATE LEVEL COURSES'),
#     ('MSC','MASTERS'),
#     ('DOC','SOME DOCTORATE LEVEL COURSES'),
#     ('PHD','DOCTORATE DEGREE'),
# )
    
# Main applicant starts here
class MainApplicant(models.Model):
    application_number = models.IntegerField(null=False, blank=False, unique=False)
    region = models.CharField(max_length=20)
    family_name = models.CharField(null=False, blank=False, max_length=255)
    first_name = models.CharField(null=False, blank=False, max_length=255)
    middle_name = models.CharField(null=False, blank=False, max_length=255)
    gender = models.CharField(max_length=10, null=True)
    month_B = models.PositiveIntegerField(max_length=255, null=True)
    day_B = models.PositiveIntegerField(blank=False, null=True)
    year_B = models.PositiveIntegerField(blank=False, null=True)
    birth_city = models.CharField(max_length=255, null=True)
    birth_country = models.CharField(max_length=255, null=True)
    eligibility_country = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True, unique=False)
    highest_education = models.CharField(max_length=255, null=True)
    no_of_children = models.PositiveIntegerField(null=True)
    marital_status = models.CharField(max_length=255, null=True)
    DisplayFields = ['id','application_number','region','family_name','first_name','middle_name','gender','month_B','day_B','year_B','birth_city','birth_country','eligibility_country','phone','email','highest_education','no_of_children','marital_status']
    SearchableFields = ['family_name','first_name']
    FilterFields = ['region']

    def __str__(self):
        return self.family_name
    
    class Meta:
        ordering = ('family_name',)
        verbose_name_plural = 'MainApplicant'
    

# Spouse details goes here
class Spouse(models.Model):
    main_applicant = models.ForeignKey(MainApplicant, on_delete=models.CASCADE)
    family_name = models.CharField(null=False, blank=False, max_length=255)
    first_name = models.CharField(null=False, blank=False, max_length=255)
    middle_name = models.CharField(null=False, blank=False, max_length=255)
    gender = models.CharField(max_length=10)
    month_B = models.DateField(max_length=255)
    day_B = models.PositiveIntegerField(blank=False)
    year_B = models.PositiveIntegerField(blank=False)
    birth_city = models.CharField(max_length=255)
    birth_country = models.CharField(max_length=255)

    def __str__(self):
        return self.main_applicant.family_name
    
    class Meta:
        ordering = ('family_name',)
        verbose_name_plural = 'Spouse'

# Children details goes here
class Children(models.Model):
    main_applicant = models.ForeignKey(MainApplicant, on_delete=models.CASCADE)
    dress_color = models.CharField(blank=False, max_length=50)
    family_name = models.CharField(null=False, blank=False, max_length=255)
    first_name = models.CharField(null=False, blank=False, max_length=255)
    middle_name = models.CharField(null=False, blank=False, max_length=255)
    gender = models.CharField(max_length=10)
    month_B = models.DateField(max_length=255)
    day_B = models.PositiveIntegerField(blank=False)
    year_B = models.PositiveIntegerField(blank=False)
    birth_city = models.CharField(max_length=255)
    birth_country = models.CharField(max_length=255)

    def __str__(self):
        return self.main_applicant.family_name
    
    class Meta:
        ordering = ('family_name',)
        verbose_name_plural = 'Children'