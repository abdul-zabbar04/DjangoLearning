from django.shortcuts import render, redirect
from .import forms
# Create your views here.
def add_category(request):
    if request.method=="POST":
        category_form= forms.CategoryForm(request.POST)
        if category_form.is_valid():
            # author_form.save()
            print(category_form)
            return redirect('categoryPage')
    else:
        category_form= forms.CategoryForm()
    return render(request, 'add_category.html', {'form': category_form})