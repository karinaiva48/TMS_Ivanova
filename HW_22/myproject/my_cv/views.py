from django.shortcuts import render

def home(request):
    return render(request, 'my_cv/home.html', {})

def skills(request):
    return render(request, 'my_cv/skills.html', {})

def education(request):
    return render(request, 'my_cv/education.html', {})

def contact(request):
    return render(request, 'my_cv/contact.html', {})
