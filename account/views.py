from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from employee.models import Employee


def registerUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        id = request.POST['employee_id']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('registerUser')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email id already taken')
                    return redirect('registerUser')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, id=id,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now register and can log in')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('registerUser')

    else:
        return render(request, 'accounts/register.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logoutUser(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def dashboardUser(request):
    user_time_entries = Employee.objects.order_by('date_time_out').filter(emp_id=request.user.id)
    context = {'time_entries': user_time_entries}
    return render(request, 'accounts/dashboard.html', context)