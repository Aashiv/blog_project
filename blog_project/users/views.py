from django.shortcuts import render, redirect






from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import JsonResponse

# Create your views here.
def register_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({"success": True, "message": "User created successfully!"}, status=200)
        else:
            # Send form errors back as JSON
            errors = form.errors.get_json_data()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('posts:list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})