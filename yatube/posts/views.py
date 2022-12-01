from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'posts/index.html'
    text_main = 'Это главная страница проекта Yatube'
    context: dict = {'text_main': text_main}
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    text_group = 'Здесь будет информация о группах проекта Yatube'
    context: dict = {'text_group': text_group}
    return render(request, template, context)
