from datetime import datetime


from django.shortcuts import render, get_object_or_404
from django.conf import settings

from blog.models import Post, Category


POSTS = Post.objects.select_related(*settings.RELATED_FIELDS)


def index(request):
    posts = POSTS.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    )[:settings.PUBS_ON_PAGE]
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, id):
    post = get_object_or_404(POSTS.filter(
                             is_published=True, category__is_published=True,
                             pub_date__lte=datetime.now()), pk=id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)
    post_list = POSTS.filter(is_published=True,
                             pub_date__lte=datetime.now(),
                             category=category)
    return render(request, 'blog/category.html', {'post_list': post_list,
                                                  'category': category})
