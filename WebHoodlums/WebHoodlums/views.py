from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from .models import UserProfile
from django.http import HttpResponse
from .models import ResumeData
# Create your views here.

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        # Check if passwords match
        if password != confirm_password:
            return JsonResponse({'success': False, 'error': 'Passwords do not match'})

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'error': 'Username already exists'})

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Optionally, you can log in the user after signup
        auth.login(request, user)

        # Return a success response
        return JsonResponse({'success': True})

    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=uname, password=password)

        if user is not None:
            # Access the has_signed_up attribute if applicable
            if hasattr(user, 'profile') and user.profile.has_signed_up:
                return JsonResponse({'success': True, 'signupCompleted': True})
            else:
                return JsonResponse({'success': True, 'signupCompleted': False})
        else:
            return JsonResponse({'success': False, 'error': 'Incorrect password or user does not exist'})
    else:
        return render(request, 'login.html')

def team(request):
    return render(request, 'OurTeam.html')


def form_view1(request):
    return render(request, 'form1.html')

def resume_view1(request):
    # Retrieve the latest entry based on the created_at field
    latest_resume_data = ResumeData.objects.order_by('-created_at').first()
    return render(request, 'resume1.html', {'latest_applicant': latest_resume_data})

def submit_form1(request):
    if request.method == 'POST':
        # Process the form data and save it to the database
        name = request.POST.get('name', '')
        designation = request.POST.get('designation', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        locationvalue = request.POST.get('locationvalue', '')
        description = request.POST.get('description', '')
        language1 = request.POST.get('language1', '')
        language2 = request.POST.get('language2', '')
        language3 = request.POST.get('language3', '')
        language4 = request.POST.get('language4', '')
        Professional_Skill_1 = request.POST.get('Professional_Skill_1', '')
        skill_range1 = int(request.POST.get('skill_range1')) if request.POST.get('skill_range1', 0) else 0
        Professional_Skill_2 = request.POST.get('Professional_Skill_2', '')
        skill_range2 = int(request.POST.get('skill_range2')) if request.POST.get('skill_range2', 0) else 0
        Professional_Skill_3 = request.POST.get('Professional_Skill_3', '')
        skill_range3 = int(request.POST.get('skill_range3')) if request.POST.get('skill_range3',  0) else 0
        Professional_Skill_4 = request.POST.get('Professional_Skill_4', '')
        skill_range4 = int(request.POST.get('skill_range4')) if request.POST.get('skill_range4', 0) else 0
        Technical_Skill_1 = request.POST.get('Technical_Skill_1', '')
        skill_range5 = int(request.POST.get('skill_range5')) if request.POST.get('skill_range5', 0) else 0
        Technical_Skill_2 = request.POST.get('Technical_Skill_2', '')
        skill_range6 = int(request.POST.get('skill_range6')) if request.POST.get('skill_range6',  0) else 0
        Technical_Skill_3 = request.POST.get('Technical_Skill_3', '')
        skill_range7 = int(request.POST.get('skill_range7')) if request.POST.get('skill_range7', 0) else 0
        Technical_Skill_4 = request.POST.get('Technical_Skill_4', '')
        skill_range8 = int(request.POST.get('skill_range8')) if request.POST.get('skill_range8', 0) else 0
        eduname1 = request.POST.get('eduname1', '')
        Uni1 = request.POST.get('Uni1', '')
        startdate = request.POST.get('startdate', '')
        enddate = request.POST.get('enddate', '')
        edudes = request.POST.get('edudes', '')
        eduname2 = request.POST.get('eduname2', '')
        Uni2 = request.POST.get('Uni2', '')
        startdate2 =request.POST.get('startdate2', '')
        enddate2 = request.POST.get('enddate2', '')
        edudes2 = request.POST.get('edudes2', '')
        eduname3 = request.POST.get('eduname3', '')
        Uni3 = request.POST.get('Uni3', '')
        startdate3 = request.POST.get('startdate3', '')
        enddate3 = request.POST.get('enddate3', '')
        edudes3 = request.POST.get('edudes3', '')
        Domain1 = request.POST.get('Domain1', '')
        Description1 = request.POST.get('Description1', '')
        Domain2 = request.POST.get('Domain2', '')
        Description2 = request.POST.get('Description2', '')
        Domain3 = request.POST.get('Domain3', '')
        Description3 = request.POST.get('Description3', '')
        Project_Name1 = request.POST.get('Project_Name1', '')
        Project_Domain1 = request.POST.get('Project_Domain1', '')
        Project_Description1 = request.POST.get('Project_Description1', '')
        url1 = request.POST.get('url1', '')
        Project_Name2 = request.POST.get('Project_Name2', '')
        Project_Domain2 = request.POST.get('Project_Domain2', '')
        Project_Description2 = request.POST.get('Project_Description2', '')
        url2 = request.POST.get('url2', '')
        Project_Name3 = request.POST.get('Project_Name3', '')
        Project_Domain3 = request.POST.get('Project_Domain3', '')
        Project_Description3 = request.POST.get('Project_Description3', '')
        url3 = request.POST.get('url3', '')

        # Save data to the database
        resume_data = ResumeData(
            name=name,
            designation=designation,
            email=email,
            contact=contact,
            locationvalue=locationvalue,
            description=description,
            language1=language1,
            language2=language2,
            language3=language3,
            language4=language4,
            Professional_Skill_1=Professional_Skill_1,
            skill_range1=skill_range1,
            Professional_Skill_2 = Professional_Skill_2,
            skill_range2=skill_range2,
            Professional_Skill_3 = Professional_Skill_3,
            skill_range3=skill_range3,
            Professional_Skill_4 = Professional_Skill_4,
            skill_range4=skill_range4,
            Technical_Skill_1 = Technical_Skill_1,
            skill_range5=skill_range5,
            Technical_Skill_2 = Technical_Skill_2,
            skill_range6=skill_range6,
            Technical_Skill_3 = Technical_Skill_3,
            skill_range7=skill_range7,
            Technical_Skill_4 = Technical_Skill_4,
            skill_range8=skill_range8,
            eduname1 = eduname1,
            Uni1 = Uni1,
            startdate = startdate,
            enddate = enddate,
            edudes = edudes,
            eduname2 = eduname2,
            Uni2 = Uni2,
            startdate2 = startdate2,
            enddate2 = enddate2,
            edudes2 = edudes2,
            eduname3 = eduname3,
            Uni3 = Uni3,
            startdate3 = startdate3,
            enddate3 = enddate3,
            edudes3 = edudes3,
            Domain1 = Domain1,
            Description1 = Description1,
            Domain2 = Domain2,
            Description2 = Description2,
            Domain3 = Domain3,
            Description3 = Description3,
            Project_Name1 = Project_Name1,
            Project_Domain1 = Project_Domain1,
            Project_Description1 = Project_Description1,
            url1 = url1,
            Project_Name2 = Project_Name2,
            Project_Domain2 = Project_Domain2,
            Project_Description2 = Project_Description2,
            url2 = url2,
            Project_Name3 = Project_Name3,
            Project_Domain3 = Project_Domain3,
            Project_Description3 = Project_Description3,
            url3 = url3,
        )
        resume_data.save()

        # Redirect to the resume page
        return redirect('resume_view1')
    else:
        # Handle the case when the form is not submitted using POST
        return HttpResponse('Invalid Request')
    
def form_view2(request):
    return render(request, 'form2.html')

def resume_view2(request):
    # Retrieve the latest entry based on the created_at field
    latest_resume_data = ResumeData.objects.order_by('-created_at').first()
    return render(request, 'resume2.html', {'latest_applicant': latest_resume_data})

def submit_form2(request):
    if request.method == 'POST':
        # Process the form data and save it to the database
        name = request.POST.get('name', '')
        designation = request.POST.get('designation', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        locationvalue = request.POST.get('locationvalue', '')
        description = request.POST.get('description', '')
        language1 = request.POST.get('language1', '')
        language2 = request.POST.get('language2', '')
        language3 = request.POST.get('language3', '')
        language4 = request.POST.get('language4', '')
        Professional_Skill_1 = request.POST.get('Professional_Skill_1', '')
        skill_range1 = int(request.POST.get('skill_range1')) if request.POST.get('skill_range1', 0) else 0
        Professional_Skill_2 = request.POST.get('Professional_Skill_2', '')
        skill_range2 = int(request.POST.get('skill_range2')) if request.POST.get('skill_range2', 0) else 0
        Professional_Skill_3 = request.POST.get('Professional_Skill_3', '')
        skill_range3 = int(request.POST.get('skill_range3')) if request.POST.get('skill_range3',  0) else 0
        Professional_Skill_4 = request.POST.get('Professional_Skill_4', '')
        skill_range4 = int(request.POST.get('skill_range4')) if request.POST.get('skill_range4', 0) else 0
        Technical_Skill_1 = request.POST.get('Technical_Skill_1', '')
        skill_range5 = int(request.POST.get('skill_range5')) if request.POST.get('skill_range5', 0) else 0
        Technical_Skill_2 = request.POST.get('Technical_Skill_2', '')
        skill_range6 = int(request.POST.get('skill_range6')) if request.POST.get('skill_range6',  0) else 0
        Technical_Skill_3 = request.POST.get('Technical_Skill_3', '')
        skill_range7 = int(request.POST.get('skill_range7')) if request.POST.get('skill_range7', 0) else 0
        Technical_Skill_4 = request.POST.get('Technical_Skill_4', '')
        skill_range8 = int(request.POST.get('skill_range8')) if request.POST.get('skill_range8', 0) else 0
        eduname1 = request.POST.get('eduname1', '')
        Uni1 = request.POST.get('Uni1', '')
        startdate = request.POST.get('startdate', '')
        enddate = request.POST.get('enddate', '')
        edudes = request.POST.get('edudes', '')
        eduname2 = request.POST.get('eduname2', '')
        Uni2 = request.POST.get('Uni2', '')
        startdate2 =request.POST.get('startdate2', '')
        enddate2 = request.POST.get('enddate2', '')
        edudes2 = request.POST.get('edudes2', '')
        eduname3 = request.POST.get('eduname3', '')
        Uni3 = request.POST.get('Uni3', '')
        startdate3 = request.POST.get('startdate3', '')
        enddate3 = request.POST.get('enddate3', '')
        edudes3 = request.POST.get('edudes3', '')
        Domain1 = request.POST.get('Domain1', '')
        Description1 = request.POST.get('Description1', '')
        Domain2 = request.POST.get('Domain2', '')
        Description2 = request.POST.get('Description2', '')
        Domain3 = request.POST.get('Domain3', '')
        Description3 = request.POST.get('Description3', '')
        Project_Name1 = request.POST.get('Project_Name1', '')
        Project_Domain1 = request.POST.get('Project_Domain1', '')
        Project_Description1 = request.POST.get('Project_Description1', '')
        url1 = request.POST.get('url1', '')
        Project_Name2 = request.POST.get('Project_Name2', '')
        Project_Domain2 = request.POST.get('Project_Domain2', '')
        Project_Description2 = request.POST.get('Project_Description2', '')
        url2 = request.POST.get('url2', '')
        Project_Name3 = request.POST.get('Project_Name3', '')
        Project_Domain3 = request.POST.get('Project_Domain3', '')
        Project_Description3 = request.POST.get('Project_Description3', '')
        url3 = request.POST.get('url3', '')

        # Save data to the database
        resume_data = ResumeData(
            name=name,
            designation=designation,
            email=email,
            contact=contact,
            locationvalue=locationvalue,
            description=description,
            language1=language1,
            language2=language2,
            language3=language3,
            language4=language4,
            Professional_Skill_1=Professional_Skill_1,
            skill_range1=skill_range1,
            Professional_Skill_2 = Professional_Skill_2,
            skill_range2=skill_range2,
            Professional_Skill_3 = Professional_Skill_3,
            skill_range3=skill_range3,
            Professional_Skill_4 = Professional_Skill_4,
            skill_range4=skill_range4,
            Technical_Skill_1 = Technical_Skill_1,
            skill_range5=skill_range5,
            Technical_Skill_2 = Technical_Skill_2,
            skill_range6=skill_range6,
            Technical_Skill_3 = Technical_Skill_3,
            skill_range7=skill_range7,
            Technical_Skill_4 = Technical_Skill_4,
            skill_range8=skill_range8,
            eduname1 = eduname1,
            Uni1 = Uni1,
            startdate = startdate,
            enddate = enddate,
            edudes = edudes,
            eduname2 = eduname2,
            Uni2 = Uni2,
            startdate2 = startdate2,
            enddate2 = enddate2,
            edudes2 = edudes2,
            eduname3 = eduname3,
            Uni3 = Uni3,
            startdate3 = startdate3,
            enddate3 = enddate3,
            edudes3 = edudes3,
            Domain1 = Domain1,
            Description1 = Description1,
            Domain2 = Domain2,
            Description2 = Description2,
            Domain3 = Domain3,
            Description3 = Description3,
            Project_Name1 = Project_Name1,
            Project_Domain1 = Project_Domain1,
            Project_Description1 = Project_Description1,
            url1 = url1,
            Project_Name2 = Project_Name2,
            Project_Domain2 = Project_Domain2,
            Project_Description2 = Project_Description2,
            url2 = url2,
            Project_Name3 = Project_Name3,
            Project_Domain3 = Project_Domain3,
            Project_Description3 = Project_Description3,
            url3 = url3,
        )
        resume_data.save()

        # Redirect to the resume page
        return redirect('resume_view2')
    else:
        # Handle the case when the form is not submitted using POST
        return HttpResponse('Invalid Request')

def form_view3(request):
    return render(request, 'form3.html')

def resume_view3(request):
    # Retrieve the latest entry based on the created_at field
    latest_resume_data = ResumeData.objects.order_by('-created_at').first()
    return render(request, 'resume3.html', {'latest_applicant': latest_resume_data})

def submit_form3(request):
    if request.method == 'POST':
        # Process the form data and save it to the database
        name = request.POST.get('name', '')
        designation = request.POST.get('designation', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        locationvalue = request.POST.get('locationvalue', '')
        description = request.POST.get('description', '')
        language1 = request.POST.get('language1', '')
        language2 = request.POST.get('language2', '')
        language3 = request.POST.get('language3', '')
        language4 = request.POST.get('language4', '')
        Professional_Skill_1 = request.POST.get('Professional_Skill_1', '')
        skill_range1 = int(request.POST.get('skill_range1')) if request.POST.get('skill_range1', 0) else 0
        Professional_Skill_2 = request.POST.get('Professional_Skill_2', '')
        skill_range2 = int(request.POST.get('skill_range2')) if request.POST.get('skill_range2', 0) else 0
        Professional_Skill_3 = request.POST.get('Professional_Skill_3', '')
        skill_range3 = int(request.POST.get('skill_range3')) if request.POST.get('skill_range3',  0) else 0
        Professional_Skill_4 = request.POST.get('Professional_Skill_4', '')
        skill_range4 = int(request.POST.get('skill_range4')) if request.POST.get('skill_range4', 0) else 0
        Technical_Skill_1 = request.POST.get('Technical_Skill_1', '')
        skill_range5 = int(request.POST.get('skill_range5')) if request.POST.get('skill_range5', 0) else 0
        Technical_Skill_2 = request.POST.get('Technical_Skill_2', '')
        skill_range6 = int(request.POST.get('skill_range6')) if request.POST.get('skill_range6',  0) else 0
        Technical_Skill_3 = request.POST.get('Technical_Skill_3', '')
        skill_range7 = int(request.POST.get('skill_range7')) if request.POST.get('skill_range7', 0) else 0
        Technical_Skill_4 = request.POST.get('Technical_Skill_4', '')
        skill_range8 = int(request.POST.get('skill_range8')) if request.POST.get('skill_range8', 0) else 0
        eduname1 = request.POST.get('eduname1', '')
        Uni1 = request.POST.get('Uni1', '')
        startdate = request.POST.get('startdate', '')
        enddate = request.POST.get('enddate', '')
        edudes = request.POST.get('edudes', '')
        eduname2 = request.POST.get('eduname2', '')
        Uni2 = request.POST.get('Uni2', '')
        startdate2 =request.POST.get('startdate2', '')
        enddate2 = request.POST.get('enddate2', '')
        edudes2 = request.POST.get('edudes2', '')
        eduname3 = request.POST.get('eduname3', '')
        Uni3 = request.POST.get('Uni3', '')
        startdate3 = request.POST.get('startdate3', '')
        enddate3 = request.POST.get('enddate3', '')
        edudes3 = request.POST.get('edudes3', '')
        Domain1 = request.POST.get('Domain1', '')
        Description1 = request.POST.get('Description1', '')
        Domain2 = request.POST.get('Domain2', '')
        Description2 = request.POST.get('Description2', '')
        Domain3 = request.POST.get('Domain3', '')
        Description3 = request.POST.get('Description3', '')
        Project_Name1 = request.POST.get('Project_Name1', '')
        Project_Domain1 = request.POST.get('Project_Domain1', '')
        Project_Description1 = request.POST.get('Project_Description1', '')
        url1 = request.POST.get('url1', '')
        Project_Name2 = request.POST.get('Project_Name2', '')
        Project_Domain2 = request.POST.get('Project_Domain2', '')
        Project_Description2 = request.POST.get('Project_Description2', '')
        url2 = request.POST.get('url2', '')
        Project_Name3 = request.POST.get('Project_Name3', '')
        Project_Domain3 = request.POST.get('Project_Domain3', '')
        Project_Description3 = request.POST.get('Project_Description3', '')
        url3 = request.POST.get('url3', '')

        # Save data to the database
        resume_data = ResumeData(
            name=name,
            designation=designation,
            email=email,
            contact=contact,
            locationvalue=locationvalue,
            description=description,
            language1=language1,
            language2=language2,
            language3=language3,
            language4=language4,
            Professional_Skill_1=Professional_Skill_1,
            skill_range1=skill_range1,
            Professional_Skill_2 = Professional_Skill_2,
            skill_range2=skill_range2,
            Professional_Skill_3 = Professional_Skill_3,
            skill_range3=skill_range3,
            Professional_Skill_4 = Professional_Skill_4,
            skill_range4=skill_range4,
            Technical_Skill_1 = Technical_Skill_1,
            skill_range5=skill_range5,
            Technical_Skill_2 = Technical_Skill_2,
            skill_range6=skill_range6,
            Technical_Skill_3 = Technical_Skill_3,
            skill_range7=skill_range7,
            Technical_Skill_4 = Technical_Skill_4,
            skill_range8=skill_range8,
            eduname1 = eduname1,
            Uni1 = Uni1,
            startdate = startdate,
            enddate = enddate,
            edudes = edudes,
            eduname2 = eduname2,
            Uni2 = Uni2,
            startdate2 = startdate2,
            enddate2 = enddate2,
            edudes2 = edudes2,
            eduname3 = eduname3,
            Uni3 = Uni3,
            startdate3 = startdate3,
            enddate3 = enddate3,
            edudes3 = edudes3,
            Domain1 = Domain1,
            Description1 = Description1,
            Domain2 = Domain2,
            Description2 = Description2,
            Domain3 = Domain3,
            Description3 = Description3,
            Project_Name1 = Project_Name1,
            Project_Domain1 = Project_Domain1,
            Project_Description1 = Project_Description1,
            url1 = url1,
            Project_Name2 = Project_Name2,
            Project_Domain2 = Project_Domain2,
            Project_Description2 = Project_Description2,
            url2 = url2,
            Project_Name3 = Project_Name3,
            Project_Domain3 = Project_Domain3,
            Project_Description3 = Project_Description3,
            url3 = url3,
        )
        resume_data.save()

        # Redirect to the resume page
        return redirect('resume_view3')
    else:
        # Handle the case when the form is not submitted using POST
        return HttpResponse('Invalid Request')
    
def form_view4(request):
    return render(request, 'form4.html')
    
def resume_view4(request):
    # Retrieve the latest entry based on the created_at field
    latest_resume_data = ResumeData.objects.order_by('-created_at').first()
    return render(request, 'resume4.html', {'latest_applicant': latest_resume_data})

def submit_form4(request):
    if request.method == 'POST':
        # Process the form data and save it to the database
        name = request.POST.get('name', '')
        designation = request.POST.get('designation', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        locationvalue = request.POST.get('locationvalue', '')
        description = request.POST.get('description', '')
        language1 = request.POST.get('language1', '')
        language2 = request.POST.get('language2', '')
        language3 = request.POST.get('language3', '')
        language4 = request.POST.get('language4', '')
        Professional_Skill_1 = request.POST.get('Professional_Skill_1', '')
        skill_range1 = int(request.POST.get('skill_range1')) if request.POST.get('skill_range1', 0) else 0
        Professional_Skill_2 = request.POST.get('Professional_Skill_2', '')
        skill_range2 = int(request.POST.get('skill_range2')) if request.POST.get('skill_range2', 0) else 0
        Professional_Skill_3 = request.POST.get('Professional_Skill_3', '')
        skill_range3 = int(request.POST.get('skill_range3')) if request.POST.get('skill_range3',  0) else 0
        Professional_Skill_4 = request.POST.get('Professional_Skill_4', '')
        skill_range4 = int(request.POST.get('skill_range4')) if request.POST.get('skill_range4', 0) else 0
        Technical_Skill_1 = request.POST.get('Technical_Skill_1', '')
        skill_range5 = int(request.POST.get('skill_range5')) if request.POST.get('skill_range5', 0) else 0
        Technical_Skill_2 = request.POST.get('Technical_Skill_2', '')
        skill_range6 = int(request.POST.get('skill_range6')) if request.POST.get('skill_range6',  0) else 0
        Technical_Skill_3 = request.POST.get('Technical_Skill_3', '')
        skill_range7 = int(request.POST.get('skill_range7')) if request.POST.get('skill_range7', 0) else 0
        Technical_Skill_4 = request.POST.get('Technical_Skill_4', '')
        skill_range8 = int(request.POST.get('skill_range8')) if request.POST.get('skill_range8', 0) else 0
        eduname1 = request.POST.get('eduname1', '')
        Uni1 = request.POST.get('Uni1', '')
        startdate = request.POST.get('startdate', '')
        enddate = request.POST.get('enddate', '')
        edudes = request.POST.get('edudes', '')
        eduname2 = request.POST.get('eduname2', '')
        Uni2 = request.POST.get('Uni2', '')
        startdate2 =request.POST.get('startdate2', '')
        enddate2 = request.POST.get('enddate2', '')
        edudes2 = request.POST.get('edudes2', '')
        eduname3 = request.POST.get('eduname3', '')
        Uni3 = request.POST.get('Uni3', '')
        startdate3 = request.POST.get('startdate3', '')
        enddate3 = request.POST.get('enddate3', '')
        edudes3 = request.POST.get('edudes3', '')
        Domain1 = request.POST.get('Domain1', '')
        Description1 = request.POST.get('Description1', '')
        Domain2 = request.POST.get('Domain2', '')
        Description2 = request.POST.get('Description2', '')
        Domain3 = request.POST.get('Domain3', '')
        Description3 = request.POST.get('Description3', '')
        Project_Name1 = request.POST.get('Project_Name1', '')
        Project_Domain1 = request.POST.get('Project_Domain1', '')
        Project_Description1 = request.POST.get('Project_Description1', '')
        url1 = request.POST.get('url1', '')
        Project_Name2 = request.POST.get('Project_Name2', '')
        Project_Domain2 = request.POST.get('Project_Domain2', '')
        Project_Description2 = request.POST.get('Project_Description2', '')
        url2 = request.POST.get('url2', '')
        Project_Name3 = request.POST.get('Project_Name3', '')
        Project_Domain3 = request.POST.get('Project_Domain3', '')
        Project_Description3 = request.POST.get('Project_Description3', '')
        url3 = request.POST.get('url3', '')

        # Save data to the database
        resume_data = ResumeData(
            name=name,
            designation=designation,
            email=email,
            contact=contact,
            locationvalue=locationvalue,
            description=description,
            language1=language1,
            language2=language2,
            language3=language3,
            language4=language4,
            Professional_Skill_1=Professional_Skill_1,
            skill_range1=skill_range1,
            Professional_Skill_2 = Professional_Skill_2,
            skill_range2=skill_range2,
            Professional_Skill_3 = Professional_Skill_3,
            skill_range3=skill_range3,
            Professional_Skill_4 = Professional_Skill_4,
            skill_range4=skill_range4,
            Technical_Skill_1 = Technical_Skill_1,
            skill_range5=skill_range5,
            Technical_Skill_2 = Technical_Skill_2,
            skill_range6=skill_range6,
            Technical_Skill_3 = Technical_Skill_3,
            skill_range7=skill_range7,
            Technical_Skill_4 = Technical_Skill_4,
            skill_range8=skill_range8,
            eduname1 = eduname1,
            Uni1 = Uni1,
            startdate = startdate,
            enddate = enddate,
            edudes = edudes,
            eduname2 = eduname2,
            Uni2 = Uni2,
            startdate2 = startdate2,
            enddate2 = enddate2,
            edudes2 = edudes2,
            eduname3 = eduname3,
            Uni3 = Uni3,
            startdate3 = startdate3,
            enddate3 = enddate3,
            edudes3 = edudes3,
            Domain1 = Domain1,
            Description1 = Description1,
            Domain2 = Domain2,
            Description2 = Description2,
            Domain3 = Domain3,
            Description3 = Description3,
            Project_Name1 = Project_Name1,
            Project_Domain1 = Project_Domain1,
            Project_Description1 = Project_Description1,
            url1 = url1,
            Project_Name2 = Project_Name2,
            Project_Domain2 = Project_Domain2,
            Project_Description2 = Project_Description2,
            url2 = url2,
            Project_Name3 = Project_Name3,
            Project_Domain3 = Project_Domain3,
            Project_Description3 = Project_Description3,
            url3 = url3,
        )
        resume_data.save()

        # Redirect to the resume page
        return redirect('resume_view4')
    else:
        # Handle the case when the form is not submitted using POST
        return HttpResponse('Invalid Request')
