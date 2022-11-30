from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('This is homepage, sun.')

def group_posts(request, slug):
    return HttpResponse(f'Post {slug} are verified by RosKomControl!')
