from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', LoginView.as_view(template_name='users/signin.html'), name='signin'),
    path('<str:username>/signout/', LogoutView.as_view(template_name='users/signout.html'), name='signout'),
    path('<int:pk>/profile/', views.profile, name='profile'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]