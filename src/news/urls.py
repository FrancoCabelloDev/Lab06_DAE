from django.urls import path
from news import views

app_name = "news"

urlpatterns = [
    # Home page with latest articles
    path("", views.ArticleListView.as_view(), name="home"),
    
    # Article detail page
    path("article/<slug:slug>/", views.ArticleDetailView.as_view(), name="article_detail"),

    # Search articles
    path('search/', views.search_articles, name='search_articles'),
]
