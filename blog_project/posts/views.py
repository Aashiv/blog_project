from django.shortcuts import render, redirect





from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.

def list(request):
    pass

def post_new(request):
    pass

def home(request):
    context = {
        "LoginForm": AuthenticationForm(),
        "RegForm": UserCreationForm()
    }
    return render(request, 'posts/home.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    return render(request, 'posts/home.html', {'form': form})

def login(request):
    pass