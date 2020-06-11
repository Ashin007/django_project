from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': "ashin",
        'title': "new post",
        "date_posted": "augest 10",
        "content": "some random content first"
    },
    {
        'author': "ashi",
        'title': "new post second",
        "date_posted": "augest 70",
        "content": "some random content second"
    }
]


def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {'title': 'about'})


