from django.shortcuts import render, redirect
from django.views import View
from .models import Article
from django.db.models import Q


class Index(View):
    template = "index.html"

    def get(self, request):
        """
        Handle GET request to fetch and display articles.

        Args:
            request: HTTP request object containing query parameters.

        Returns:
            Response: Rendered HTML template with filtered articles if a query is provided,
                      or all articles if no query is given.
        """
        query = request.GET.get("query", "")
        if query:
            articles = Article.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        else:
            articles = Article.objects.all()
        return render(request, self.template, {"articles": articles})


class AddArticle(View):
    template = "add-article.html"

    def get(self, request):
        """
        Handle GET request to display the add-article form.

        Args:
            request: HTTP request object.

        Returns:
            Response: Rendered HTML template displaying the add-article form.
        """
        return render(request, self.template)

    def post(self, request):
        """
        Handle POST request to create a new article.

        Args:
            request: HTTP request object containing article data.

        Returns:
            Response: Redirect to the index page after successfully creating a new article.
        """
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.POST.get("author")
        Article.objects.create(title=title, content=content, author=author)
        return redirect("index")


class Agb(View):
    template = "agb.html"

    def get(self, request):
        """
        Handle GET request to display the AGB page.

        Args:
            request: HTTP request object.

        Returns:
            Response: Rendered HTML template displaying the AGB (terms and conditions) page.
        """
        return render(request, self.template)


class LegalNotice(View):
    template = "legal-notice.html"

    def get(self, request):
        """
        Handle GET request to display the legal notice page.

        Args:
            request: HTTP request object.

        Returns:
            Response: Rendered HTML template displaying the legal notice page.
        """
        return render(request, self.template)
