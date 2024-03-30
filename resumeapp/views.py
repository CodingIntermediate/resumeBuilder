from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegForm,UserForm,companyLoginForm,usersLoginForm,VacancyForm,InterviewForm
from .models import RegModel,UserModel,VacancyModel,JobApplication,InterviewDetails,ChatModel
from datetime import datetime
from django.contrib.auth import logout
from django.db.models import Q
from django.http import HttpResponse
# from django.contrib import message
# below code is for company registeration view by admin
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
# def edit(request,regid):
#     if request.method == 'POST':
#         mydata = RegModel.objects.get(regid=regid)
#         form = RegForm(request.POST, instance=mydata)
#         if form.is_valid():
#             form.save()
#             return redirect('dataview')  # Redirect to a success page after saving
#     else:
#         mydat=RegModel.objects.get(regid=regid)
#         form = RegForm(instance=mydat)
#     return render(request,'edit.html',{'forms': form})  # Render the form for GET requests       
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
                    users = UserModel.objects.get(Email=Email,Password=Password)
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
    return render(request, 'CompanyPage.html')
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
# create a function for vacancy_view by admin
def vacancy_view(request):
    dataVacancy=VacancyModel.objects.all()
    return render(request,'VacancyTable.html',{'datasVacancy': dataVacancy})
# create a function for edit and delete for vacancy for admin
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
    application=JobApplication(job_id=vid,application_id=applicant)
    application.save()
    return redirect('Jobs')
# ================================================================================
# create a function for applied users
def appliedusers(request):
    regid=request.session.get('regid')
    # print(regid)
    comp=VacancyModel.objects.get(regid=regid)
    # print(comp)
    appliedusers=JobApplication.objects.filter(job_id=comp)
    # my_var=UserModel.objects.all()
    # paired_data=zip(appliedusers,my_var)
    # print(appliedusers)
    return render(request,'Appliedusers.html',{'appliedusers': appliedusers})
# not completed
# ================================================================================
# create a logout function for companies
def logouts(request):
    logout(request)
    return redirect('index')
#-----------------------------------------
# create vacancy_view function viewed by that particular firms
def viewedByParticularCompanies(request):
    companySession=request.session.get('regid')
    vacancyData=VacancyModel.objects.filter(regid=companySession)
    return render(request,'VacancyTable.html',{'data':vacancyData})
# ================================================================================
# creat a function to view the profile of comapny data
def comapanyProfile(request):
    prof=request.session.get('regid')
    comProf=RegModel.objects.filter(regid=prof)
    return render(request,'viewCompanyProfile.html',{'data':comProf})  
# ---------------------------------------------------------------
# create a function editProfile for comapnies
def editCompanyProfile(request,regid):
    if request.method == 'POST':
        mydata = RegModel.objects.get(regid=regid)
        form = RegForm(request.POST, instance=mydata)
        if form.is_valid():
            form.save()
            return redirect('viewCompanyProfile')  # Redirect to a success page after saving
    else:
        mydat=RegModel.objects.get(regid=regid)
        form = RegForm(instance=mydat)
    return render(request,'EditCompanyProfile.html',{'forms': form}) 
# ================================================================================
# create a function to view the profile of user data
def userProfile(request) :
    user=request.session.get('userid')
    userProf=UserModel.objects.filter(userid=user)
    return render(request,'viewUserProfile.html',{'data':userProf})
# -----------------------------------------------------------------
# create a function editUserProfile for users
def editUserProfile(request,userid):
    if request.method == 'POST':
        mydata = UserModel.objects.get(userid=userid)
        form = UserForm(request.POST, instance=mydata)
        if form.is_valid():
            form.save()
            return redirect('viewUserProfile')  # Redirect to a success page after saving
    else:
        mydat=UserModel.objects.get(userid=userid)
        form = UserForm(instance=mydat)
    return render(request,'EditUserProfile.html',{'forms': form}) 
# ================================================================================ 
# create a function applied jobs by users

def viewappliedjobs(request):
    user=request.session.get('userid')
    userProf=JobApplication.objects.filter(candidate_id=user)
    return render(request,'Appliedjobs.html',{'data':userProf})
# -----------------------------------------------------------------------
# create a cancel of job by user
def cancel(request,application_id):
    cancl=get_object_or_404(JobApplication,application_id=application_id)
    cancl.canacel='1'
    cancl.save()
    return redirect('Appliedjobs')
# ================================================================================
# create a function to view the notification of job canceled of users notified to companies 
# ================================================================================
# create a view for company ,addInterviewDetails
def addInterviewDetails(request,application_id):
    varible=JobApplication.objects.get(application_id=application_id)
    # sess = request.session.get('regid')
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            varibl = form.save(commit=False)
            varibl.application_id = varible
            varibl.save()
            return redirect('CompanyPage')   
    else:
        form = InterviewForm()
    return render(request, 'AddInterviewDetails.html', {'interw_details': form})
# ------------------------------------------------------------------
# cteate a function to view the interview details for users
def interviewDetails(request, application_id):
    user_id = request.session.get('userid')
    # user = UserModel.objects.get(userid=user_id)
    interview_details = InterviewDetails.objects.filter(application_id=application_id)
    return render(request, 'InterviewDetails.html', {'interDetails': interview_details}) 
# ------------------------------------------------------------------
# create a function for editInterviewDetails
def editInterviewDetails(request,application_id):
    if request.method == 'POST':
        mydata = InterviewDetails.objects.get(application_id=application_id)
        form = InterviewForm(request.POST, instance=mydata)
        if form.is_valid():
            form.save()
            return redirect('Appliedusers')  # Redirect to a success page after saving
    else:
        mydat=InterviewDetails.objects.get(application_id=application_id)
        form = InterviewForm(instance=mydat)
    return render(request,'EditInterviewDetails.html',{'interviewEdit': form})
# ------------------------------------------------------------------
# create a view for search jobs
def searchjobs(request):
    query = request.GET.get('search', '')  # Get the search term from the GET request
    if query:  # If there's a search term
        jobs = VacancyModel.objects.filter(
            Q(Job_Category__icontains=query) |
            Q(Job_Name__icontains=query) |
            Q(Job_Details__icontains=query)
        )
    else:  # If there's no search term
        jobs = VacancyModel.objects.all()  # Display all jobs or none, as per your preference

    return render(request, 'Jobs.html', {'jobs': jobs, 'query': query})

# ------------------------------------------------------------------
# create a chat page
def chat(request,application_id):
    # Assuming 'regid' is stored in the session to identify the sender
    sender_id = request.session.get('regid')
    sender = get_object_or_404(RegModel, regid=sender_id)
    
    # Retrieve the JobApplication and indirectly the receiver
    job_application = get_object_or_404(JobApplication, application_id=application_id)
    receiver = job_application.candidate_id    

    if request.method == 'POST':
        message = request.POST.get('msg')
        # Create the chat message
        ChatModel.objects.create(sender=sender, receiver=receiver, message=message)
        return HttpResponse("Message sent successfully")
    else:
        # GET request handling or initial page load
        return render(request, 'chat.html') 
# ------------------------------------------------------------------
# ------------------------------------------------------------------
#create a complaint view
def complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            sender_id = request.session.get('userid')
            if sender_id:
                complnt = form.save(commit=False)
                # Fetch the UserModel instance using sender_id
                sender_instance = get_object_or_404(UserModel, pk=sender_id)
                # Assign the UserModel instance to complnt.sender_id
                complnt.sender_id = sender_instance
                complnt.save()
                return redirect('UserPage')
    else:
        form = ComplaintForm()
    return render(request, 'complaint.html', {'form': form})
#
