from django.shortcuts import render, get_object_or_404
from .models import Category,News
from django.http import Http404
# Create your views here.


def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list':news_list
    }

    return render(request, "news/news_list.html", context=context)

def news_detail(request,id):
    news = get_object_or_404(News, id=id,status=News.Status.Published)
    context = {
        'news':news
    }

    return render(request,"news/news_detail.html", context=context)


def HomePageView(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:3]
    local_1 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[1]
    local_2 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[2]
    local_3 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[3]
    local_4 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[4]
    sport_1 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[1]
    sport_2= News.published.all().filter(category__name="Sport").order_by("-publish_time")[2]
    sport_3 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[3]
    sport_4 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[4]
    fan_texnika_1 = News.published.all().filter(category__name="Fan-texnika").order_by("-publish_time")[1]
    fan_texnika_2 = News.published.all().filter(category__name="Fan-texnika").order_by("-publish_time")[2]
    fan_texnika_3 = News.published.all().filter(category__name="Fan-texnika").order_by("-publish_time")[3]
    fan_texnika_4 = News.published.all().filter(category__name="Fan-texnika").order_by("-publish_time")[4]
    jahon_one = News.published.all().filter(category__name="Jahon").order_by("-publish_time")

    context = {
        "news_list":news_list,
        "categories":categories,
        "local_1":local_1,
        "local_2": local_2,
        "local_3": local_3,
        "local_4": local_4,
        "sport_1":sport_1,
        "sport_2": sport_2,
        "sport_3": sport_3,
        "sport_4": sport_4,
        "fan_texnika_1":fan_texnika_1,
        "fan_texnika_2": fan_texnika_2,
        "fan_texnika_3": fan_texnika_3,
        "fan_texnika_4": fan_texnika_4,
        "jahon_one":jahon_one
    }

    return render(request, 'news/index.html',context)


