from django.views.generic import ListView, DetailView
from .models import Article, Category

class ArticleListView(ListView):
    model = Article
    template_name = "news/home.html"
    context_object_name = "latest_articles"

    def get_queryset(self):
        return Article.objects.filter(status="published")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["recent_articles"] = Article.objects.filter(status="published").order_by("-published_date")[:5]
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = "news/article_detail.html"
    context_object_name = "article"

    def get_queryset(self):
        return Article.objects.filter(status="published")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["recent_articles"] = Article.objects.filter(status="published").order_by("-published_date")[:5]
        return context
