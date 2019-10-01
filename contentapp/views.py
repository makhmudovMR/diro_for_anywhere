from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

def get_banner():
    return models.Banner.objects.all()

def get_bannerlink():
    return models.BannerLinks.objects.all()


def home_view(request):
    newses = models.News.objects.all().order_by('-date')[:5]
    files = models.Files.objects.all().order_by('-id')[:5]
    for i in range(len(newses)):
        # print(newses[i].text)
        newses[i].text = newses[i].text.replace('<p>&nbsp;</p>', '').replace('<p style="text-align:center">&nbsp;</p>', '').replace('<p style="text-align:right">&nbsp;</p>', '').replace('&nbsp;', '')
        # print(newses[i].text)
    context = {
        'files': files,
        'newses': newses,
        'banners': get_banner(),
        'bannerlink': get_bannerlink(),
    }
    return render(request, 'contentapp/home.html', context)


def news_detail_view(request, id):
    item = models.News.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, 'contentapp/news_detail.html', context)


def news_view(request):
    newses = models.News.objects.all().order_by('-date')
    paginator = Paginator(newses, 10)
    page = request.GET.get('page')
    for i in range(len(newses)):
        # print(newses[i].text)
        newses[i].text = newses[i].text.replace('<p>&nbsp;</p>', '').replace('<p style="text-align:center">&nbsp;</p>', '').replace('<p style="text-align:right">&nbsp;</p>', '').replace('&nbsp;', '')
        # print(newses[i].text)

    try:
        newses = paginator.page(page)
    except PageNotAnInteger:
        newses = paginator.page(1)
    except EmptyPage:
        newses = paginator.page(paginator.num_pages)

    context = {
        'newses': newses,
    }

    return render(request, 'contentapp/news.html', context)


def files_view(request):
    files = models.Files.objects.all().order_by('-id')

    paginator = Paginator(files, 10)
    page = request.GET.get('page')

    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    context = {
        'files': files
    }

    return render(request, 'contentapp/files.html', context)


def search_result_view(request):
    words = request.GET.get('words')

    founded_newses = models.News.objects.filter(Q(title__icontains=words)|Q(text__icontains=words))
    founded_files = models.Files.objects.filter(Q(name__icontains=words)|Q(description__icontains=words))

    for i in range(len(founded_newses)):
        founded_newses[i].text = founded_newses[i].text.replace('<p>&nbsp;</p>', '').replace('<p style="text-align:center">&nbsp;</p>', '').replace('<p style="text-align:right">&nbsp;</p>', '').replace('&nbsp;', '')

    context = {
        'newses': founded_newses,
        'files': founded_files,
    }

    return render(request, 'contentapp/search_result.html', context)

