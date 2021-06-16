from django.shortcuts import render, get_object_or_404
from posts.models import Category, Post


def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'header': "Категории"
    }
    return render(request, 'posts/index.html', context)


def category_list(request, category_slug):
    categories = Category.objects.all()
    category = get_object_or_404(categories, slug=category_slug)
    posts = Post.objects.filter(category=category).order_by('weight')
    context = {
        'posts': posts,
        'header': "Категория " + category.name,
        'breadcrumb': {
            'breadcrumb_level': 'category',
            'category': {
                'name': category.name,
                'slug': category.slug
            },
        },
        'categories': categories,
    }
    return render(request, 'posts/posts.html', context)


def post(request, category_slug, post_slug):
    category = get_object_or_404(Category, slug=category_slug)
    category_posts = Post.objects.filter(category=category).order_by('weight')
    _post = get_object_or_404(category_posts ,slug=post_slug)
    context = {
        'post': _post,
        'header': _post.title,
        'breadcrumb': {
            'breadcrumb_level': 'post',
            'category': {
                'name': category.name,
                'slug': category.slug
            },
            'post': _post.title,
        },
        'category_posts': category_posts,
    }
    return render(request, 'posts/post.html', context)
