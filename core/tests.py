from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.management import call_command
from core.management.commands.initdb import Command
from core.models import Product

# Create your tests here.


# Command
class TestCommand(TestCase):
    # Test that products are fetched from OFF's database
    @patch('core.management.commands.initdb.requests.get')
    def test_initdb(self, mock_requests):
        mock_requests.get.return_value = {
            "code": "123456789",
            "product_name_fr": "product1",
            "nutriscore_grade": "a",
            "image_url": "ND",
            "url": "ND",
            "energy-kj_100g": "ND",
            "fat_100g": "ND",
            "saturated-fat_100g": "ND",
            "salt_100g": "ND",
            "carbohydrates_100g": "ND",
            "fiber_100g": "ND",
            "sugars_100g": "ND",
            "proteins_100g": "ND",
        }
        # result = mock_requests.get.return_value

        '''def json(self):
            return {
                "products": [
                    {
                        "code": result["code"],
                        "product_name_fr": result["product_name_fr"],
                        "nutriscore_grade": result["nutriscore_grade"],
                        "image_url": "ND",
                        "url": "ND",
                        "nutriments": {
                            "energy-kj_100g": "ND",
                            "fat_100g": "ND",
                            "saturated-fat_100g": "ND",
                            "salt_100g": "ND",
                            "carbohydrates_100g": "ND",
                            "fiber_100g": "ND",
                            "sugars_100g": "ND",
                            "proteins_100g": "ND",
                        }
                    }
                ]
            }'''

        call_command("initdb", cat_file="categories", amount="1")
        print(Product.objects.all())
        assert Product.objects.get(product_code='123456789').product_name_fr ==  mock_requests.get.return_value.product_name_fr


# Index page
class TestHomePageView(TestCase):
    # test that index page returns a 200
    def test_homepage(self):
        response = self.client.get(reverse("/"))
        self.assertEqual(response.status_code, 200)


# Users
class TestUser(TestCase):
    # test that user is created
    def test_user_signup(self):
        # response in setup ?
        response = self.client.post(
            "/signup/",
            {
                "username": "john",
                "email": "johnsmith@pbmail.com",
                "password1": "smith1234",
                "password2": "smith1234",
            },
        )
        user = User.objects.get(username="john")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(user.username, "john")

    # test user can log in
    def test_user_login(self):
        self.client.post(
            "/signup/",
            {
                "username": "john",
                "email": "johnsmith@pbmail.com",
                "password1": "smith1234",
                "password2": "smith1234",
            },
        )
        response_login = self.client.post(
            "/login/", {"username": "john", "password1": "smith1234"}
        )
        self.assertEqual(response_login.status_code, 200)
        login = self.client.login(username="john", password="smith1234")
        self.assertEqual(login, True)


# User page
class TestAccountView(TestCase):
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

    # test page returns 200 if user is connected
    def test_account(self):
        self.client.login(username="john", password="smith1234")
        response = self.client.get("/account/john")
        self.assertEqual(response.status_code, 200)

    # test redirection if user not connected
    def test_account_redirect_login(self):
        response = self.client.get("/account/AnonymousUser", follow=True)
        self.assertEqual(
            response.redirect_chain, [("/login/?next=/account/AnonymousUser", 302)]
        )
