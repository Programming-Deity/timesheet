from django.contrib import messages, auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm
from employee.models import Employee




def registerUser(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            id = form.cleaned_data['employee_id']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create(username=username, password=password, email=email, id=id,
                                            first_name=first_name, last_name=last_name)
            user.save()
            messages.success(request, 'You are now register and can log in')
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})






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


@login_required(login_url='login')
def dashboardUser(request):
    user_time_entries = Employee.objects.order_by('date_time_out').filter(emp_id=request.user.id)
    context = {'time_entries': user_time_entries}
    return render(request, 'accounts/dashboard.html', context)