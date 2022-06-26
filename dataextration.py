from tkinter import image_names
from unicodedata import category

from numpy import product
from requests_html import HTMLSession
import wget

base_url = 'https://www.amazon.com/ref=nav_logo'
category = "Video Games"
example_product = "https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/ref=lp_16225016011_1_1"

def get_page_content(url):
    session = HTMLSession()
    return session.get(url).html

def get_product_data(content):
    return {
        "name": content.find(".product-name")[0].text,
        "code": content.find(".product-code")[0].text,
        "price": content.find(".price-box")[0].text,
        "image-url": content.find(".js-product-image")[0].attrs["src"],
        "description": content.find(".tab-contents")[0].text,

    }

content = get_page_content(base_url + category + "/" + example_product)
product_data = get_product_data(content)

print(product_data)

