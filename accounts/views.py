from django.shortcuts import redirect, reverse, render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from home.views import index
from accounts.forms import UserLoginForm

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
