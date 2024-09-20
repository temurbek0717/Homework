from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from .models import News, Category

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list':news_list
    }

    return render(request, "news/news_list.html",context=context)


class HomePageView(TemplateView):
    template_name = "news/index.html"

class CategoryPageView(TemplateView):
    template_name = "news/category.html"


class SinglePageView(TemplateView):
    template_name = "news/single.html"

class CantactPageView(TemplateView):
    template_name = "news/contact.html"

