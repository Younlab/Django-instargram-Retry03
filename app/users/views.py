from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('users:sign-in')
    else:
        return render(request, 'sign/sign_in.html')
