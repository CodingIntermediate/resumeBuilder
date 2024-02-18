from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegForm,UserForm,companyLoginForm,usersLoginForm
from .models import RegModel,UserModel

# below code is for inpurt or add new values
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
# above code is for company registeration ,ends here
# below code is for view the enterd data to the users
def reaData(request):  
    dataObject=RegModel.objects.all()
    return render(request,'dataview.html',{'datas': dataObject})
# below code is for view the enterd data to the users  ,ends here
# all the above code functions are for only companies
# from line 7 to 20 are for comapnyregisteratiin and view the registered comapnies
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
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
# below code is for to view registered users
def userData(request):
    datasObject=UserModel.objects.all()
    return render(request,'usersData.html',{'usersdata': datasObject})
# from line 27 to 39 are user registeratiin  and view them
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# create 2 functions for accept and reject done by admin for companies
def accept(request,regid):
    # regid camed from RegModels(models)
    accpt=get_object_or_404(RegModel,regid=regid)
    accpt.Status='1'
    accpt.save() # for redirection not need .html extension
    return redirect('dataview')

def reject(request,regid):
    rejct=get_object_or_404(RegModel,regid=regid)
    rejct.Status='0'
    rejct.save()
    return redirect('dataview')
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# to view adminpanel
def admin(request):
    return render(request,'AdminPanel.html')
# to view adminpanel,ends
# from line 44 to 45 ,all the above adminpanel section datas are viwed by here admin
# =============================================================================================
# =================================================================================================
# =============================================================================================
# login page for companies
# create a function companyLogin
def companyLogin(request):
    return render(request,'companyLogin.html')

# authenticate a function for login(companies or users)
def logins(request,usertype):
    if usertype =="company":
        if request.method == 'POST':
            form = companyLoginForm(request.POST)
            if form.is_valid():
                Email = form.cleaned_data['Email']
                Password = form.cleaned_data['Password']
                try:
                    companies = RegModel.objects.get(Email=Email,Password=Password)
                    request.session['regid'] = companies.regid
                    return redirect('usersData')
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
                    return redirect('dataview')
                except UserModel.DoesNotExist:
                    form.add_error(None, 'Invalid username or password.')
        else:
            form = usersLoginForm()
        return render(request,'Login.html',{'loginform': form})



   
# ===========================================================================================

