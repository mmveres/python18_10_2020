import logging

from ua.python18_10_2020.univer.lesson07.product import Product
from datetime import datetime
logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("Product")

def get_3_product():
    products = []
    log.debug("try create 3 product")
    try:
        products.append(Product("apple1", 15, 25))
        products.append(Product("apple2", 10, 20))
        products.append(Product("apple3", 20, 15))
    except Exception as e:
        log.error(f"Error {e}")
        raise e
    log.debug("Create 3 product")
    return products

if __name__ == '__main__':
    products = get_3_product()

    for product in products:
        print(product)
