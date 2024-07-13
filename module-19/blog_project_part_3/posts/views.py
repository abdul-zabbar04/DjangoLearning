from django.shortcuts import render, redirect
from .import forms
from .import models
from django.contrib.auth.decorators import login_required


# for class based views:
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.

# @login_required
# def add_post(request):
#     if request.method=="POST":
#         post_form= forms.PostForm(request.POST)
#         if post_form.is_valid():
#             post_form.instance.author= request.user
#             post_form.save()
#             return redirect('add_post')
#     else:
#         post_form= forms.PostForm()
#     return render(request, 'add_post.html', {'form': post_form})

# create/post using class based view:

@method_decorator(login_required, name='dispatch')
class add_post(CreateView):
    model= models.Post
    form_class= forms.PostForm
    template_name= "add_post.html"
    success_url = reverse_lazy("add_post")
    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)

          

# @login_required
# def edit_post(request, id):
#     target_post= models.Post.objects.get(pk= id)
#     # print(target_post.title)
#     post_form = forms.PostForm(instance=target_post)
#     if request.method=="POST":
#         post_form= forms.PostForm(request.POST, instance=target_post)
#         if post_form.is_valid():
#             post_form.instance.author= request.user # aita na dileu
#             #hoto, because author edit korar access user passe na. jeta instance a deya cilo oitai always thake. aber 
#             # akhane onno user o edit korar sujog nai. so, aita
#             #  dile o ja na dilo o tai. just ai case ar khetre.
#             post_form.save()
#             return redirect('profile')
        
#     return render(request, 'add_post.html', {'form': post_form})

@method_decorator(login_required, name='dispatch')
class editView(UpdateView):
    model= models.Post
    form_class= forms.PostForm
    template_name= 'add_post.html'
    pk_url_kwarg= 'id'
    success_url= reverse_lazy('profile')
    



# @login_required
# def delete_post(request, id):
#     target_post= models.Post.objects.get(pk= id).delete()
#     # print(target_post.title)
#     return redirect('profile')
 
@method_decorator(login_required, name='dispatch')   
class delete_view(DeleteView):
    model= models.Post
    template_name= 'delete.html'
    pk_url_kwarg= 'id'
    success_url= reverse_lazy('profile')

class post_details(DetailView):
    model= models.Post
    template_name='post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form= forms.CommentForm(data= self.request.POST)
        post= self.get_object()
        if comment_form.is_valid():
            new_comment= comment_form.save(commit=False)
            new_comment.post= post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context=  super().get_context_data(**kwargs)
        post= self.object
        comments= post.comments.all()     
        comment_form= forms.CommentForm()
        context['comments']= comments
        context['comment_form']= comment_form
        return context