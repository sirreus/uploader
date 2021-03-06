from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request):
    context = {
        "title": "Detail"
    }
    return render(request, 'posts/index.html', context)

def post_list(request):
    context = {
        "title": "List"
    }
    return render(request, 'posts/index.html', context)

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
