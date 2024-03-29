from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.contrib.auth.models import User


# 主頁
def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 驗證
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "登入成功！")
            return redirect('home')
        else:
            messages.success(request, "登入失敗，請再重新輸入一次！")
            return redirect('home')

    return render(request, 'home.html', {'records': records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "您已登出成功！")

    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            # 驗證
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']            
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "註冊成功！")

            return redirect('home')
    
    else:
        form = SignUpForm()

        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # 尋找客戶紀錄
        customer_record = Record.objects.get(id=pk)

        return render(request, 'record.html', {'customer_record': customer_record})
    
    else:
        messages.success(request, "你需要登入才能查看此頁面...")
        
        return redirect('home')
    

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "刪除成功！")
        return redirect('home')

    else:
        messages.success(request, "你需要登入才能刪除...")
        return redirect('home')
    

def add_record(request):
    form =  AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "紀錄新增成功！")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    
    else:
        messages.success(request, "你需要登入才能新增...")
        return redirect('home')
    

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)        
        if form.is_valid():
            form.save()
            messages.success(request, "更新成功！")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    
    else:
        messages.success(request, "你需要登入才能更新...")
        return redirect('home')