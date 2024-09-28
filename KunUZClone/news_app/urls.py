from django.urls import path
from .views import  HomePageView, news_detail, news_list





urlpatterns = [
    path('',HomePageView,name="homepage"),
    path('news/',news_list, name="news_all"),
    path("news/<int:id>/",news_detail, name='news_detail_page'),


]