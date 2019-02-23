from django.http import Http404
from django.shortcuts import render

from myblog.models import Post


def splash(request):
    return render(request, "splash.html")


def index(request):
    post = Post.objects.order_by('date')
    return render(request, "index.html", {'result': post})


def detail(request, post_title):
    try:
        post = Post.objects.get(title=post_title)
    except Post.DoesNotExist:
        raise Http404("Sorry :(")
    return render(request, "detail.html", {'result': post})
