from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context: dict = {
        'posts': posts,
        'title': 'This is main page of Yatube'
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context: dict = {
        'group': group,
        'posts': posts,
        'title': 'Записи сообщества ' + f'"{group.title}"'
    }
    return render(request, 'posts/group_list.html', context)
