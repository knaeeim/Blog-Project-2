from django.shortcuts import render, redirect
from .forms import PostForm
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                form.instance.author = request.user
                form.save()
                messages.success(request, "Post added successfully")
                return redirect('home')
        else:
            form = PostForm()
        return render(request, "add_post.html", {'form': form})

@login_required
def edit_post(request, id):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=id)
        # print(post)
        form = PostForm(instance=post)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.instance.author = request.user
                form.save()
                messages.success(request, "Post updated successfully")
                return redirect('home')
        return render(request, "edit_post.html", {'form': form})

@login_required
def delete_post(request, id):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=id)
        # print(post)
        messages.success(request, "Post deleted successfully")
        post.delete()
        return redirect('home')