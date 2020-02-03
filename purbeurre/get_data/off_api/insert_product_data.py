'''code responsible for the insertion of products data into tables'''
from ..models import Product


class ProductData:

    @staticmethod
    def insert_product_data(data):
        for product in data['products']:
            save_data = Product.objects.create(
                product_code=product.get('code', None),
                product_name=product.get('product_name_fr', 'ND'),
                product_nutriscore=product.get('nutriscore_grade', 'ND'),
                product_image_url=product.get('image_url', 'ND'),
                product_url=product.get('url', 'ND'),
                # #nutriments##
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
                    'fibers_100g', 'ND'
                    ),
                product_sugars_100g=product['nutriments'].get(
                    'sugars_100g', 'ND'
                    ),
                product_proteins_100g=product['nutriments'].get(
                    'proteins_100g', 'ND'
                    ),
                )
            return save_data
