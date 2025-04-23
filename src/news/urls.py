from django.urls import path
from .views import ArticleListView, ArticleDetailView

app_name = 'news'

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
]
