from django.shortcuts import render, redirect
from .import forms
from .import models
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def add_post(request):
    if request.method=="POST":
        post_form= forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author= request.user
            post_form.save()
            return redirect('add_post')
    else:
        post_form= forms.PostForm()
    return render(request, 'add_post.html', {'form': post_form})

@login_required
def edit_post(request, id):
    target_post= models.Post.objects.get(pk= id)
    # print(target_post.title)
    post_form = forms.PostForm(instance=target_post)
    if request.method=="POST":
        post_form= forms.PostForm(request.POST, instance=target_post)
        if post_form.is_valid():
            post_form.instance.author= request.user # aita na dileu
            #hoto, because author edit korar access user passe na. jeta instance a deya cilo oitai always thake. aber 
            # akhane onno user o edit korar sujog nai. so, aita
            #  dile o ja na dilo o tai. just ai case ar khetre.
            post_form.save()
            return redirect('profile')
        
    return render(request, 'add_post.html', {'form': post_form})

@login_required
def delete_post(request, id):
    target_post= models.Post.objects.get(pk= id).delete()
    # print(target_post.title)
    return redirect('profile')
        
