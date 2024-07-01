from django.shortcuts import render, redirect
from .import forms
from .import models

# Create your views here.
def add_post(request):
    if request.method=="POST":
        post_form= forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form= forms.PostForm()
    return render(request, 'add_post.html', {'form': post_form})

def edit_post(request, id):
    target_post= models.Post.objects.get(pk= id)
    # print(target_post.title)
    post_form = forms.PostForm(instance=target_post)
    if request.method=="POST":
        post_form= forms.PostForm(request.POST, instance=target_post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homePage')
        
    return render(request, 'add_post.html', {'form': post_form})

def delete_post(request, id):
    target_post= models.Post.objects.get(pk= id).delete()
    # print(target_post.title)
    return redirect('homePage')
        
