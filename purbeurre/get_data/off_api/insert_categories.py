
from ..models import Category


class Categories:

    @staticmethod
    def insert_categories(categories):
        for category in categories:
            save_cat = Category.objects.create(category_name=category)
            return save_cat
