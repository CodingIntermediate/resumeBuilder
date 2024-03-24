from django.urls import path

from.import views  
urlpatterns=[
    # entire details are view only by AdminPanel
    path('AdminPanel/',views.admin,name='AdminPanel'),
    # this one is for compamy registeration
    path('register/',views.companyRegister,name='register'),
    # below one for register_companie view
    path('companyTable',views.companyTable,name='companyTable'),
    # below one for user registration
    path('userRegister/',views.userRegister,name='userRegister'),
    # userRegistered datas are catched by below line code
    path('userTable',views.userTable,name='userTable'),
    # page redirection for accept and reject
    path('approve/<int:regid>',views.accept,name='accept'),
    path('reject/<int:regid>',views.reject,name='reject'),
    # below code for login (users or companies)
    path('Login/<str:usertype>/',views.logins,name='Login'),
    # path('sucess/',views.sucess,name='sucess'),
    path('UserPage/',views.HomeUsers,name='UserPage'),
    path('CompanyPage/',views.CompanyPage,name='CompanyPage'),
    # path('edit/<int:regid>',views.edit,name='edit'),
    path('edituser/<int:userid>',views.edituser,name='edituser'),
    path('deletedataview/<int:regid>',views.deletedata,name='deletedataview'),
    path('deleteusers/<int:userid>',views.deleteusers,name='deleteusers'), 
    path('companyuserviews',views.company_user_view,name='companyuserviews'),
    # path('card',views.card,name='card'),
    # approve reject for users
    path('approveusers/<int:userid>',views.acceptusers,name='acceptusers'),
    path('rejectusers/<int:userid>',views.rejectusers,name='rejectusers'),
    # -------------------------------------------------
    # for vacancy
    path('Vacancy/',views.vacancyadding,name='Vacancy'), 
    path('VacancyTable/',views.viewedByParticularCompanies,name='VacancyTable'),
    path('editvacancy/<int:pk>',views.editvacancy,name='editvacancy'),
    path('deletevacancy/<int:pk>',views.deletevacancy,name='deletevacancy'),
    # -------------------------------------------------
    # for users
    path('Jobs/',views.Job,name='Jobs'),
    
    # applii users id
    path('apply/<int:pk>',views.apply,name='apply'),
    
    # index page
    path('',views.indexPage,name='index'), 
    
    # applicants
    path('Appliedusers/',views.appliedusers,name='Appliedusers'),
    # logout path
    path('logouts/',views.logouts,name='logouts'),
    # -------------------------------------------------
    # view Company profile
    path('viewCompanyProfile/',views.comapanyProfile,name='viewCompanyProfile'),
    # edit companyProfile
    path('editCompanyProfile/<int:regid>',views.editCompanyProfile,name='editCompanyProfile'),
    # -------------------------------------------------
    # view user Profile
    path('viewUserProfile',views.userProfile,name='viewUserProfile'),
     # edit userProfile
    path('editUserProfile/<int:userid>',views.editUserProfile,name='editUserProfile'),
    # -------------------------------------------------
    
    # view applied jobs by  users
    path('Appliedjobs/',views.viewappliedjobs,name='Appliedjobs'),
    # cancel jobs for users
    path('cancel/<int:application_id>',views.cancel,name='cancel'),
    
    # addinterviewDetails View
    path('AddInterviewDetails/<int:application_id>',views.addInterviewDetails,name='AddInterviewDetails'),
    
    # interviewDetails View
    path('InterviewDetails/<int:application_id>',views.interviewDetails,name='InterviewDetails'),
    
    # edit interview details
    path('editInterviewDetails/<int:application_id>',views.editInterviewDetails,name='editInterviewDetails'),
    
    # create a path for search
    path('Jobs/',views.searchjobs,name='Jobs'),
    path('search/', views.searchjobs, name='search'),
    # chat
    path('chat/<int:application_id>',views.chat,name='chat'),
    # # mssage send 
    # path('chat/', views.chat_view, name='chat'),
    # path('chatmessage/<int:application_id>/', views.chatmessage, name='chatmessage'),

] 