'''call to the openfoodfacts api'''


from .insert_product_data import ProductData
import requests


class Call:

    AMOUNT = '200'
    category_list = [
        'barres-chocolatees', 'boissons-avec-sucre-ajoute', 'desserts-glaces',
        'desserts-lactes', 'desserts-au-chocolat', 'chocolats',
        'viennoiseries', 'bonbons', 'confiseries-chocolatees',
        'pates-a-tartiner', 'laits-aromatises', 'nectars-d-orange',
        'nectars-de-pomme', 'jus-de-pomme',
        'jus-de-fruits-a-base-de-concentre', 'jus-d-orange',
        'jus-multifruits', 'pizzas', 'pizzas-surgelees',
        'plats-prepares-frais', 'box', 'pates-instantanees',
        'lasagnes-preparees', 'plats-au-boeuf', 'plats-a-la-volaille'
    ]

    @staticmethod
    def fetch_data(category, amount):
        url = (
                f"https://fr.openfoodfacts.org/cgi/search.pl?action=process"
                f"&tagtype_0=categories&tag_contains_0=contains"
                f"&tag_0={category}&sort_by=unique_scans_n"
                f"&page_size={amount}&json=1"
            )
        response = requests.get(url)
        data = response.json()
        return data

    def insert_data():
        for category in Call.category_list:
            data = Call.fetch_data(category, Call.AMOUNT)
            ProductData.insert_product_data(data)
