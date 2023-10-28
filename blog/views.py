from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogCreationForm, BlogUpdateForm
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView

def blogs(request):
    blogs = Blog.objects.all()
    context = {
        'title' : 'Blogs',
        'blogs' : blogs,
    }
    return render(request, 'blog/blogs.html', context)

def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        'title' : blog.title,
        'blog' : blog,
    }
    return render(request, 'blog/detail.html', context)

@login_required
def new(request):
    if request.method == 'POST':
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, f"Blog added successfully!")
            return redirect('blogs')
    else:
        form = BlogCreationForm()
    return render(request, 'blog/new.html', {'title' : 'New Blog', 'form' : form })

#This is my class based update view
# class BlogUpdateView(UpdateView):
#     model = Blog
#     template_name = 'blog/update.html'
#     fields = ['title', 'content']
#     success_url = reverse_lazy('blogs')

def update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.user != blog.author:
        return redirect('access_denied')

    if request.method == 'POST':
        form = BlogUpdateForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, f"Blog updated successfully!")
            return redirect('blogs')
    else:
        form = BlogUpdateForm(instance=blog)
    return render(request, 'blog/update.html', {'title' : f"{blog.title} Update", 'form' : form })

# This are my class based delete view
# class BlogDeleteView(DeleteView):
#     model = Blog
#     template_name = 'blog/delete.html'
#     success_url = reverse_lazy('blogs')


def delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.user != blog.author:
        return redirect('access_denied')
    return render(request, 'blog/delete.html', {'title' : f'Delete blog {blog.pk}', 'blog' : blog })

def delete_confirm(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.user != blog.author:
        return redirect('access_denied')
    blog.delete()
    messages.info(request, f'Blog deleted succesfully!')
    return redirect('blogs')

def access_denied(request):
    context = {
        'title' : 'Access Denied',
    }
    return render(request, 'blog/access_denied.html', context)
    

