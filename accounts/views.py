from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Remove "@login_required(login_url='login') " to allow self registration 
# Remove comment-out in _navbar.html
@login_required(login_url='login') 
def register(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            # Check username or email exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already used')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already used')
                    return redirect('register')
                else:
                    # Create the User
                    user = User.objects.create_user(username=username, email=email, password=password)
                    # Auto Login on success
                    auth.login(request, user)
                    messages.success(request, 'You are logged in')
                    return redirect('index')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged In')
            return redirect('videos')
        else:
            messages.error(request, 'Invalid Username or Password') 
            return redirect('login')
    else:        
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged Out')
        return redirect('index')

