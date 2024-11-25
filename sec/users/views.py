from django.contrib import auth
from django.shortcuts import render

from .forms import UserLoginForm


# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.autenticate(username=username, password=password)
            if user:
                auth.login(request, user)
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)
# form = ProfileForm(data=request.POST, instance=request.user,
# files=request.FILES)
#     if form.is_valid():
#         form.save()
