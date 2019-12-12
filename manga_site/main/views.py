from django.shortcuts import render
from django.http import HttpResponse
from main.models import *
from django.core.paginator import Paginator
from django.contrib import auth
from django.shortcuts import redirect
from datetime import datetime


def hel(requrest):
    manga = Manga.objects.filter()
    tag = Tags.objects.filter()
    aut = Author.objects.all()
    current_page = Paginator(manga, 5)
    page = requrest.GET.get('page')
    con = current_page.get_page(page)
    return render(requrest,'main\head.html', {'manga' : con,'Tag':tag,'user': auth.get_user(requrest),'aut':aut})


def tags(requrest):
    tag = requrest.GET
    man = Manga.objects.all()
    tags = Tags.objects.filter()
    aut = Author.objects.all()
    ex = []
    for i,j in tag.items():
        if (i=='data' and j != ''):
            man = man.filter(data_reliz=j)
        if (i=='auth'):
            man = man.filter(author = j)
        if (j == 'on'):
            ex.append(int(i))
            man = man.filter(tag=i)
    pagin = Paginator(man,5)
    page = requrest.GET.get('page')
    con = pagin.get_page(page)
    return render(requrest,'main/head.html', {'manga' : con,'Tag':tags,"check":ex,'user': auth.get_user(requrest),'aut':aut})


def such(requrest):
    get = requrest.GET['such']
    man = Manga.objects.filter(name__icontains=get)
    aut = Author.objects.all()
    tag = Tags.objects.filter()
    if(len(man) != 0):
        return render(requrest,'main/head.html', {'manga' : man,'Tag':tag,'user': auth.get_user(requrest),'aut':aut})
    else:
        return render(requrest,'main/err.html', {'manga' : man,'Tag':tag,'user': auth.get_user(requrest),'aut':aut})



def glava(requrest):
    get = requrest.GET['manga']
    man = Manga.objects.get(id=get)
    galas = man.glava.order_by('-numver')
    comnet = Coments.objects.filter(article_id=get)
    comnet = comnet.order_by('-pub_date')
    print(comnet)
    return render(requrest,'main/reads.html',{'manga':man,'user': auth.get_user(requrest),'coments':comnet,'glv':galas})


def reads(requrest):
    get = requrest.GET['glava']
    pic = Pics.objects.filter(glava=get)
    pic = pic.order_by('pic')
    return render(requrest,'main/read.html',{'imp':pic,'user': auth.get_user(requrest)})


def logut(requrest):
    auth.logout(requrest)
    return redirect('/')

def login(requrest):
    if requrest.POST:
        username = requrest.POST.get('login')
        password = requrest.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(requrest,user)
            return redirect('/')
        else:
            aut = Author.objects.all()
            tag = Tags.objects.all()
            man = Manga.objects.all()
            return render(requrest,'main/head.html',{'err':'не верное имя или пароль','manga' : man,'Tag':tag,'user': auth.get_user(requrest),'aut':aut})
    else:
        return redirect('/')

def add_coment(requrest):
    print(requrest.POST)
    if requrest.POST:
        user = requrest.POST.get('user')
        manga = requrest.POST.get('manga')
        text  = requrest.POST.get('text')
        data = requrest.POST.get('data')
        print(user,manga,text,data)
        coment = Coments()
        coment.author_id = User.objects.get(id=user)
        coment.article_id = Manga.objects.get(id=manga)
        coment.content = text
        coment.pub_date = data
        coment.save()
    return redirect('/')
