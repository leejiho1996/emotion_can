from .forms import UserForm
from django.contrib.auth import authenticate, login # 사용자 인증과 로그인 담당
from django.shortcuts import render, redirect
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # 폼의 입력값을 개별적으로 얻을떄 사용
            raw_password = form.cleaned_data.get('password1') # 폼의 입력값을 개별적으로 얻을떄 사용
            user = authenticate(username = username, password = raw_password) # 사용자 인증
            login(request, user) # 로그인
            return redirect('index')
    else:
        form = UserForm()
        # context = {'form': form}
    return render(request, 'common/signup.html', {'form':form})