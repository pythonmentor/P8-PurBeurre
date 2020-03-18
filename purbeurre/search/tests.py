from django.test import TestCase
from core.models import Category, Product
from django.urls import reverse


# Create your tests here.


# Research page
class TestSearchView(TestCase):
    def setUp(self):
        Category.objects.create(category_name="box")

        Product.objects.create(
            product_code="123456789",
            product_name="product1",
            product_category=Category.objects.get(category_name="box"),
            product_nutriscore="e",
            product_image_url="https://via.placeholder.com/150",
            product_url="https://via.placeholder.com/150",
        )
        Product.objects.create(
            product_code="987654321",
            product_name="product2",
            product_category=Category.objects.get(category_name="box"),
            product_nutriscore="a",
            product_image_url="https://via.placeholder.com/150",
            product_url="https://via.placeholder.com/150",
        )

    # test that research page returns 200
    def test_research_page(self):
        response = self.client.get(reverse("search"), {"query": " "})
        self.assertEqual(response.status_code, 200)

    # test that page returns products if correspondance is found
    def test_search_result(self):
        response = self.client.get(reverse("search"), {"query": "prod"})
        self.assertEqual(response.context["results"][0].product_code, 123456789)


# Detail Page
class TestDetailView(TestCase):
    def setUp(self):
        Category.objects.create(category_name="box")

        Product.objects.create(
            product_code="123456789",
            product_name="product1",
            product_category=Category.objects.get(category_name="box"),
            product_nutriscore="e",
            product_image_url="https://via.placeholder.com/150",
            product_url="https://via.placeholder.com/150",
        )

    # test that detail page returns a 200 if the item exists
    def test_detail_page(self):
        response = self.client.get('/search/detail/123456789')
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the item does not exist
    def test_detail_no_item(self):
        response = self.client.get("search/detail/111111111")
        self.assertEqual(response.status_code, 404)
