
from ..models import Category


class Categories:

    @staticmethod
    def insert_categories(category):
        save_cat = Category.objects.create(category_name=category)
        print('ok cat')
        return save_cat
