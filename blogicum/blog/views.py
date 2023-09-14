from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Q
from datetime import datetime

from blog.models import Post, Category


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lt=datetime.now()
    )[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        Q(pk=pk)
        & Q(is_published=True)
        & Q(category__is_published=True)
        & Q(pub_date__lt=datetime.now()),
    )

    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    post_list = get_list_or_404(
        Post.objects.select_related('category').filter(
            category__slug=category_slug,
            is_published=True,
            pub_date__lt=datetime.now()
        ),
        category__is_published=True,
    )
    category = Category.objects.get(slug=category_slug)
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
