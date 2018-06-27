from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from .forms import SignupForm
User = get_user_model()

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

def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

# def handle_uploaded_file(f):
#     with open('profile_image/profile_image', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():

            users = form.sign_up()
            login(request, users)
            return redirect('index')

    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'sign/sign_up.html', context)