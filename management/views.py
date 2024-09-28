from django.shortcuts import render, redirect
from .models import Role
from django.core.paginator import Paginator


def role_list(request):
    roles = Role.objects.all()

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        roles = roles.filter(name__icontains=search_query)

    paginator = Paginator(roles, 10)  # Paginate roles, 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'roles/role_list.html', {'page_obj': page_obj, 'search_query': search_query})


def add_role(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department = request.POST.get('department')
        platform_access = request.POST.get('platform_access')

        role = Role.objects.create(name=name, department=department, platform_access=platform_access)
        return redirect('role_list')

    return render(request, 'roles/add_role.html')
