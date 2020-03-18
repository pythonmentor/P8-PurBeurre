from core.models import Category, Product
from django.test import TestCase
from django.urls import reverse

# Create your tests here.


# Favorites page
class TestFavoriteView(TestCase):
    def setUp(self):
        self.client.post(
            "/signup/",
            {
                "username": "john",
                "email": "johnsmith@pbmail.com",
                "password1": "smith1234",
                "password2": "smith1234",
            },
        )
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

    # test page returns 200 if user is connected
    def test_logged_in(self):
        self.client.login(username="john", password="smith1234")
        response = self.client.get("/account/john")
        self.assertEqual(response.status_code, 200)

    # test page returns saved products
    def test_save_products(self):
        self.client.login(username="john", password="smith1234")
        self.client.post("/search/substitutes/", {"code": "987654321"})
        response = self.client.get(reverse("favorites"))
        self.assertEqual(response.context["favs"][0].product_id, 987654321)

    # test redirection if anonymous user
    def test_redirect_favorites(self):
        response = self.client.get(reverse("favorites"), follow=True)
        self.assertEqual(response.redirect_chain, [("/login/?next=/favorites/", 302)])


# Substitute Page
class TestSubstituteView(TestCase):
    def setUp(self):
        self.client.post(
            "/signup/",
            {
                "username": "john",
                "email": "johnsmith@pbmail.com",
                "password1": "smith1234",
                "password2": "smith1234",
            },
        )
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

    # test that sub page returns sub and 200 if subs exists
    def test_page(self):
        response = self.client.get(
            "/search/substitutes/",
            {"code": "123456789", "category": "box", "nutriscore": "e"},
        )
        self.assertEqual(response.status_code, 200)
        # print(response.context['to_sub'].product_code)
        # print(response.context['subs'][0].product_code)
        self.assertEqual(response.context["subs"][0].product_code, 987654321)

    # test that a product cannot be added twice
    def test_add_product_twice(self):
        self.client.login(username="john", password="smith1234")
        response = self.client.post(
            "/search/substitutes/", {"code": "987654321"}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            "/search/substitutes/", {"code": "987654321"}, follow=True
        )
        self.assertEqual(response.status_code, 400)

    # test only logged in users can save products
    def test_add_product_signedout(self):
        response = self.client.post(
            "/search/substitutes/", {"code": "987654321"}, follow=True
        )
        self.assertEqual(response.status_code, 400)
