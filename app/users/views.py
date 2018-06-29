from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from .forms import SignupForm
User = get_user_model()

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # 인증이 통과한 경우
        if user is not None:

            # session_id값을 django_sessions테이블에 저장, 데이터는 user와 연결됨
            # 이 함수 실행 후 돌려줄 HTTP Response에는 Set-Cookie헤더 추가, 내용은 sessionid=<session값>
            login(request, user)

            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('index')
        else:
            return redirect('users:sign-in')
    else:
        return render(request, 'sign/sign_in.html')

def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

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

def delete_user(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user.delete()
    return redirect('index')
# pk를 받는다는 것은 무슨 의미?
def follow_toggle(request):
    """
    GET 요청은 처리하지않는다.
    POST 요청일때
        request.POST로 'user.pk'값을 전달받음
            pk가 user_pk인 User를 user에 전달
        request
    :param request:
    :return:
    """
    pass