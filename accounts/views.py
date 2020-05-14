from django.shortcuts import redirect, reverse, render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from home.views import index
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User

# Create your views here.


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect(reverse('index'))


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form = UserLoginForm()
                messages.error(request, "Username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    if request.user.is_authenticated:
        messages.error(request, "You are already logged in")
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            messages.success(request, "Your account has been created")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                messages.error(
                    request, "Something went wrong, please try again")
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {"registration_form": registration_form})


def user_profile(request):
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
