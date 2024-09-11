from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.loginUser, name='login'),
    path('register', views.registerUser, name='register'),
    path('logout', views.logoutUser, name='logout'),
    path('dashboard', views.dashboardUser, name='dashboard'),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name='forgot_password/password_reset.html'), name='reset_password'),
    path('reset_passsword_sent', auth_views.PasswordResetDoneView.as_view(template_name='forgot_password/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='forgot_password/password_reset_form.html'), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='forgot_password/password_reset_complete.html'), name='password_reset_complete')
]