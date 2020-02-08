from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from myblog.models import Post


def splash(request):
    return render(request, "splash.html")


def index(request):
    post = Post.objects.order_by('date')
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 5)
    try:
        post_page = paginator.page(page)
    except PageNotAnInteger:
        post_page = paginator.page(1)
    except EmptyPage:
        post_page = paginator.page(paginator.num_pages)
    return render(request, "index.html", {'result': post_page})


def detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Sorry :(")
    return render(request, "detail.html", {'result': post})
