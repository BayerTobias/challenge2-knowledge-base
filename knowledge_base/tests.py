from django.test import TestCase
from django.urls import reverse
from .models import Article


class TestViews(TestCase):

    def setUp(self):
        Article.objects.create(
            title="Test Article 1", content="Content 1", author="Author"
        )
        Article.objects.create(
            title="Test Article 2", content="Content 2", author="Author"
        )

    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Article 1")
        self.assertContains(response, "Test Article 2")

    def test_index_view_with_query(self):
        response = self.client.get(reverse("index"), {"query": "Article 1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Article 1")
        self.assertNotContains(response, "Test Article 2")

    def test_add_article_view_get(self):
        response = self.client.get(reverse("add-article"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add-article.html")

    def test_add_article_view_post(self):
        response = self.client.post(
            reverse("add-article"),
            {"title": "New Article", "content": "New Content", "author": "New Author"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.count(), 3)
        self.assertTrue(Article.objects.filter(title="New Article").exists())

    def test_agb_view(self):
        response = self.client.get(reverse("agb"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "agb.html")

    def test_legal_notice_view(self):
        response = self.client.get(reverse("legal-notice"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "legal-notice.html")
