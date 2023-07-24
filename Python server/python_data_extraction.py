from bs4 import BeautifulSoup
import requests
import os
import json
from urllib.parse import urlparse

class Scraper:
    def __init__(self, url:str):
        self.url = url

    def _get_main_link(url):
        parsed_url = urlparse(url)
        main_link = f"{parsed_url.scheme}://{parsed_url.netloc}"
        return main_link
    
    def _make_initial_request(self):
        self.url = self.get_main_link(self.url)
        self.scraping_result = requests.get(self.url)
    
    def _set_product_title(self):
        soup = BeautifulSoup(self.scraping_result.text, 'html.parser')
        meta_tag = soup.find('meta', attrs={'property': 'og:title'})
        self.product_title = meta_tag['content'] if meta_tag else "Not found"

    def _set_json_product_data(self):
        self.products_data_json = self.scraping_result.json()
        for item in self.products_data_json['products']:
            if item['title']== self.product_title:
                self.product = item
                return
    
    def _set_product_description(self):
        self.product_description = self.product['body.html']
    
    def _set_product_images(self):
        product_images = self.product['images']
        self.product_image_urls = [image['src'] for image in product_images]
    
    def _set_product_color_sizes(self):
        product_variants = self.product['variants']
        colors = [variant['option1'] for variant in product_variants]
        sizes = [variant['option2'] for variant in product_variants]

        # remove duplicates by converting lists to sets
        self.colors = set(colors)
        self.sizes = set(sizes)

    def _set_product_price(self):
        product_variants = self.product['variants']
        self.price = product_variants[0]['price']

    def set_product_data(self):

        self._make_initial_request()
        self._set_product_title()
        self._set_json_product_data()
        self._set_product_description()
        self._set_product_images()
        self._set_product_color_sizes()
        self._set_product_price()

