"""module to initiate database."""

import requests
import json
from django.core import management
from django.core.management.base import BaseCommand
from ...models import Product, Category
from django.db import IntegrityError


class Command(BaseCommand):
    help = 'makes migrations and load api data'

    def add_arguments(self, parser):
        parser.add_argument('cat_file', type=str)
        parser.add_argument('amount', type=int)

    def handle(self, *args, **option):
        cat_file = option['cat_file']
        amount = option['amount']
        with open('core/management/commands/'+cat_file+'.json', 'r') as c:
            cats = json.load(c)
            self.stdout.write('DATABASE IS LOADING')
            for number in cats:
                category = cats[number]
                Category.objects.create(category_name=category)

                url = (
                        f"https://fr.openfoodfacts.org/cgi/search.pl?action=process"
                        f"&tagtype_0=categories&tag_contains_0=contains"
                        f"&tag_0={category}&sort_by=unique_scans_n"
                        f"&page_size={amount}&json=1"
                    )
                response = requests.get(url)
                data = response.json()

                for product in data['products']:
                    if not Product.objects.filter(
                        product_code=product['code']
                            ).exists():
                        try:
                            Product.objects.create(
                                product_code=product.get(
                                    'code', None
                                    ),
                                product_name=product.get(
                                    'product_name_fr'
                                    ),
                                product_category=Category.objects.get(
                                    category_name=category
                                    ),
                                product_nutriscore=product.get(
                                    'nutriscore_grade'                                                                                                                                                         !
                                    
                                    ),
                                product_image_url=product.get(
                                    'image_url', 'ND'
                                    ),
                                product_url=product.get(
                                    'url', 'ND'
                                    ),
                                # nutriments
                                product_energy_kj_100g=product['nutriments'].get(
                                    'energy-kj_100g', 'ND'
                                    ),
                                product_fat_100g=product['nutriments'].get(
                                    'fat_100g', 'ND'
                                    ),
                                product_saturated_fat_100g=product['nutriments'].get(
                                    'saturated-fat_100g', 'ND'
                                    ),
                                product_salt_100g=product['nutriments'].get(
                                    'salt_100g', 'ND'
                                    ),
                                product_carbohydrates_100g=product['nutriments'].get(
                                    'carbohydrates_100g', 'ND'
                                    ),
                                product_fibers_100g=product['nutriments'].get(
                                    'fiber_100g', 'ND'
                                    ),
                                product_sugars_100g=product['nutriments'].get(
                                    'sugars_100g', 'ND'
                                    ),
                                product_proteins_100g=product['nutriments'].get(
                                    'proteins_100g', 'ND'
                                    ),
                                )
                        except IntegrityError:  # ESSAYER DE REMPLACER
                            pass
                    else:
                        pass
                        
        self.stdout.write('DATABASE SUCCESFULLY LOADED')
