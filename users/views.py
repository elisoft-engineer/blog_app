from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import UserSignupForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, f"Account created successfully! for {user.username}")
            return redirect('signin')
    else:
        form = UserSignupForm()
    return render(request, 'users/signup.html', {'title' : 'Sign Up', 'form' : form })

def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile updated successfully!")
            return redirect(reverse('profile', args=[user.pk]))
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)
    return render(request, 'users/profile.html', {'given_user' : user, 'title' : 'View Profile', 'u_form' : u_form, 'p_form' : p_form })