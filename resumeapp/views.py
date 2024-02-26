from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegForm,UserForm,companyLoginForm,usersLoginForm,VacancyForm
from .models import RegModel,UserModel,VacancyModel,JobApplication
from datetime import datetime

# below code is for company registeration
def companyRegister(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')  
    else:
        form = RegForm()
    return render(request, 'register.html',{'forms': form}) 
# -------------------------------------------------------------------------------
# below code is to view the registered companies for admin
def companyTable(request):  
    dataObject=RegModel.objects.all()
    return render(request,'CompanyTable.html',{'datas': dataObject})
# -------------------------------------------------------------------------------
# create 2 functions for accept and reject done by admin for companies
def accept(request,regid):
    # regid camed from RegModels(models)
    accpt=get_object_or_404(RegModel,regid=regid)
    accpt.Status='1'
    accpt.save() # for redirection not need .html extension
    return redirect('companyTable')

def reject(request,regid):
    rejct=get_object_or_404(RegModel,regid=regid)
    rejct.Status='0'
    rejct.save()
    return redirect('companyTable')
# ---------------------------------------------------------------------------
# create 2 functions for edit and delete done by admin for companies
def edit(request,regid):
    if request.method == 'POST':
        mydata = RegModel.objects.get(regid=regid)
        form = RegForm(request.POST, instance=mydata)
        if form.is_valid():
            form.save()
            return redirect('dataview')  # Redirect to a success page after saving
    else:
        mydat=RegModel.objects.get(regid=regid)
        form = RegForm(instance=mydat)
    return render(request,'edit.html',{'forms': form})  # Render the form for GET requests       
# delete function
def deletedata(request,regid):
    # if request.method == 'POST':
    mydata = RegModel.objects.get(regid=regid)
    mydata.delete()
    return redirect('dataview')   
# =====================================================----------==========================++++++
# =====================================================----------==========================++++++
# userregisteration goes ,here 
def userRegister(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userRegister')  
    else:
        usrform = UserForm()
    return render(request, 'userRegister.html',{'userforms': usrform}) 
# -------------------------------------------------------------------------------
# below code is to  view registered users for company
def userTable(request): 
    datasObject=UserModel.objects.all()
    return render(request,'UserTable.html',{'usersdata': datasObject})
# --------------------------------------------------
# create 2 functions for edit and delete by company for users
def edituser(request,userid):
    if request.method == 'POST':
        mydata = UserModel.objects.get(userid=userid)
        form = UserForm(request.POST, instance=mydata)
        if form.is_valid():
            form.save()
            return redirect('usersData')  # Redirect to a success page after saving
    else:
        mydata=UserModel.objects.get(userid=userid)
        form = UserForm(instance=mydata)
    return render(request,'edituser.html',{'forms': form})  # Render the form for GET requests    

def deleteusers(request,userid):
    users = UserModel.objects.get(userid=userid)
    users.delete()
    return redirect('usersData')
# -------------------------------------------------------------
# create 2 functions approve and reject by company for user
def acceptusers(request,userid):
    accpt=get_object_or_404(UserModel,userid=userid)
    accpt.Status='1'
    accpt.save()
    return redirect('companyuserviews')
def rejectusers(request,userid):
    rejct=get_object_or_404(UserModel,userid=userid)
    rejct.Status='0'
    rejct.save()
    return redirect('companyuserviews')
# -------------------------------------------------------------
# ===========================================================================================
# authenticate(login) a function for login(companies or users)
def logins(request,usertype):
    if usertype =="company":
        if request.method == 'POST':
            form = companyLoginForm(request.POST)
            if form.is_valid():
                Email = form.cleaned_data['Email']
                Password = form.cleaned_data['Password']
                try:
                    companies = RegModel.objects.get(Email=Email,Password=Password,Status='1')
                    #request.session['variable']=companies.attribute
                    request.session['regid'] = companies.regid
                    return redirect('CompanyPage')
                except RegModel.DoesNotExist:
                    form.add_error(None, 'Invalid username or password.')
        else:
            form = companyLoginForm()
        return render(request,'Login.html',{'loginform': form})
    
    if usertype =="User":
        if request.method == 'POST':
            form = usersLoginForm(request.POST)
            if form.is_valid():
                Email = form.cleaned_data['Email']
                Password = form.cleaned_data['Password']
                try:
                    users = UserModel.objects.get(Email=Email,Password=Password,Status='1')
                    request.session['userid'] = users.userid
                    return redirect('UserPage')
                except UserModel.DoesNotExist:
                    form.add_error(None, 'Invalid username or password.')
        else:
            form = usersLoginForm()
        return render(request,'Login.html',{'loginform': form})  
# ================================================================================================== 
# -------------------------------------------------------------------
# to view adminpanel
def admin(request):
    return render(request,'AdminPanel.html')
#--------------------------------------------------
#create HomeUsers function
def HomeUsers(request):
    return render(request,'UserPage.html')
# function for ComanyPage
def CompanyPage(request):
    return render(request,'CompanyPage.html')
# ---------------------------------------------------
# function for user datas view by comapny
def company_user_view(request): 
    datasObject=UserModel.objects.all()
    return render(request,'companyuserviews.html',{'usersdata': datasObject})

# create an index page
def indexPage(request):
    return render(request,'index.html')  
# ================================================================================================
# create a function vacancyadding by companies
def vacancyadding(request):
    sess = request.session.get('regid')
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            # Fetch the RegModel instance corresponding to the ID in `sess`
            reg_instance = get_object_or_404(RegModel, pk=sess)
            var.regid = reg_instance
            var.save()
            return redirect('Vacancy')  
    else:
        form = VacancyForm()
    return render(request, 'Vacancy.html', {'addvacancy': form})
# create a function for vacancy_view
def vacancy_view(request):
    dataVacancy=VacancyModel.objects.all()
    return render(request,'VacancyTable.html',{'datasVacancy': dataVacancy})
# create a function for edit and delete for vacancy
def editvacancy(request,pk):
    if request.method == 'POST':
        vdata = VacancyModel.objects.get(pk=pk)
        form = VacancyForm(request.POST, instance=vdata)
        if form.is_valid():
            form.save()
            return redirect('VacancyTable')  # Redirect to a success page after saving
    else:
        vdata=VacancyModel.objects.get(pk=pk)
        form = VacancyForm(instance=vdata)
    return render(request,'editvacancy.html',{'forms': form})

def deletevacancy(request,pk):
    vacancydata=VacancyModel.objects.get(pk=pk)
    vacancydata.delete()
    return redirect('VacancyTable')
# ==========================================================================

# create a function to view available jobs(vacancy) for users
def Job(request):
    dataVacancy=VacancyModel.objects.all()
    return render(request,'Jobs.html',{'datasVacancy': dataVacancy}) 

#create a function to apply for  users and get the id of applied users
def apply(request,pk):
    # here pk is default id of vacancy
    applicant_id=request.session.get('userid')
    applicant=UserModel.objects.get(pk=applicant_id)
    vid=VacancyModel.objects.get(pk=pk)
    application=JobApplication(job_id=vid,candidate_id=applicant)
    application.save()
    return redirect('Jobs')
# ================================================================================
# create a function for applied users
def appliedusers(request):
    applicant_users=JobApplication.objects.all()
    return render(request,'appliedusers.html',{'appliedusers': applicant_users})

    