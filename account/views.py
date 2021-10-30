from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Account


# login/out, password change, and ratings preferences
# Remove "@login_required(login_url='login') " to allow self registration
# Remove comment-out in _navbar.html if needed

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
        return render(request, 'account/register.html')

def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged In')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged Out')
        return redirect('index')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/password.html', {
        'form': form
    })

# user ratings preferencing 

class UserUpdate(UpdateView):
    model = Account
    fields = ['see_pg13', 'see_r']
    template_name = 'account/user_update.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

class Pg13Update(UpdateView):
    model = Account
    fields = ['see_pg13']
    template_name = 'account/pg13_update.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
