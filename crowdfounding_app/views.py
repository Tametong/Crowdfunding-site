from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from .models import Project, Contribution
from .forms import ProjectForm, ContributionForm
from django.contrib.auth.models import User
from decimal import Decimal


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'crowdfounding/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    contributions = project.contributions.all()
    return render(request, 'crowdfounding/project_detail.html', {
        'project': project,
        'contributions': contributions
    })

@login_required
def project_create(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        goal_amount = request.POST.get('goal_amount')

        project = Project(title=title, description=description, goal_amount=goal_amount)
        project.creator = request.user
        project.save()
        return redirect('project_list')
   
    return render(request, 'crowdfounding/project_form.html')

@login_required
def contribute(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        contribution = Contribution()
        contribution.amount = Decimal(request.POST.get("contribution"))
        contribution.project = project
        contribution.contributor = request.user

        if contribution.project.current_amount + contribution.amount > contribution.project.goal_amount:
            return render(request, 'crowdfounding/contribute.html', {'project': project, 'error':'Vous ne pouvez pas contribuer une somme supérieurà celle restante'})
        
        contribution.save()
        project.current_amount += contribution.amount
        project.save()

        
            
        return redirect('project_detail', pk=project.pk)


    return render(request, 'crowdfounding/contribute.html', {'project': project})

def about_us(request):
    return render(request, 'crowdfounding/about.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('project_list')
        else:
            return render(request, 'crowdfounding/login.html', {'error': 'Erreur de connexion'})

    return render(request, 'crowdfounding/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('project_list')
        else:
            return render(request, 'crowdfounding/signup.html', {'error':'Verifiez vos informations'})

    return render(request, 'crowdfounding/signup.html')

def logout_user(request):
    logout(request)
    return redirect('project_list')