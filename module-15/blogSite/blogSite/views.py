from django.shortcuts import render
from posts.models import PostModel
def home(request):
    all_posts= PostModel.objects.all()
    # print(all_posts)
    return render(request, 'home.html', {'data': all_posts})