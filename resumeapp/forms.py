from django import forms
from .models import RegModel,UserModel,LoginModel


# below regform class is for companies ,starts here
class RegForm(forms.ModelForm):
    # above.modelform was in-built

    # below uppecases are  for dropdown selection
    STATES=(
        ('selected','Select'),
        ('keralam','Kerala'),
        ('tamilndu','Tamil Nadu'),
        ('antra','Andhra Pradesh')
    )
    states=forms.ChoiceField(choices=STATES,widget=forms.Select())

    CITIES=(
        ('selected','Select'),
        ('ador','Adoor'),
        ('kotarkra','Kottarakara'),
        ('kotym','Kottayam')
    )
    cities=forms.ChoiceField(choices=CITIES,widget=forms.Select())
    # above uppecases are  for dropdown selection


    class Meta:
        model=RegModel
        fields=['Organization_Category','Business_Name','Address','States','Cities','Pincode','Number','Email','Password']
        # the above 2 lines are already we learned
        widgets={
            'Organization_Category':forms.TextInput(),
            'Business_Name':forms.TextInput(),
            'Address':forms.TextInput(),
            'States':forms.TextInput(),
            'Cities':forms.TextInput(),
            'Pincode':forms.NumberInput(),
            'Number':forms.NumberInput(),
            'Email':forms.EmailInput(),
            'Password':forms.PasswordInput()
        }
# above regform class is for ompanies ,ends here
# # ------------------------------------------------------------------------------------------------------------------
# below userform class is for users,starts here
class UserForm(forms.ModelForm):
    GENDER=(
        # ('selected','Select'),
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    )
    Gender=forms.ChoiceField(choices=GENDER,widget=forms.RadioSelect())
    class Meta:
        model=UserModel
        fields=['Name','Gender','Date_Of_Birth','Education','Skills','Conatact_Number','Email','Password']   
        widgets={
            'Name':forms.TextInput(),
            'Gender':forms.Select(),
            'Date_Of_Birth':forms.NumberInput(),
            'Education':forms.TextInput(),
            'Skills':forms.TextInput(),
            'Conatact_Number':forms.NumberInput(),
            'Email':forms.EmailInput(),
            'Password':forms.PasswordInput()
        }     


# for login(companies)
class companyLoginForm(forms.ModelForm):
    class Meta:
        model=LoginModel
        fields=['Email','Password']   
        widgets={
            'Email':forms.EmailInput(),
            'Password':forms.PasswordInput(),
        }     
# login for users
class usersLoginForm(forms.ModelForm):
    class Meta:
        model=LoginModel
        fields=['Email','Password']   
        widgets={
            'Email':forms.EmailInput(),
            'Password':forms.PasswordInput(),
        }     
