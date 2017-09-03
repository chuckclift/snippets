from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Snippet, Tag
from django.contrib.auth import authenticate, login, logout



def index(request):
    if request.user.is_authenticated():
        post_list = Snippet.objects.order_by('pub_date').filter(author=request.user)
        context = {"snippets":post_list}
    else:
        post_list = Snippet.objects.order_by('pub_date').filter(public=True)
        context = {"snippets":post_list}
        


    return render(request, 'cut/index.html', context) 

def create_post(request):
    if request.method == "POST" and request.user.is_authenticated():
        Snippet.objects.create(content=request.POST.get("content"), author=request.user)
    return HttpResponseRedirect("/")



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
    elif request.method == "GET":
        return render(request, "cut/login.html")

    return HttpResponseRedirect("/")
            
def logout_user(request):
    if request.user.is_authenticated():
        logout(request)
    return HttpResponseRedirect("/")

