import logging

from ua.python18_10_2020.univer.lesson07.currency import Currency
from ua.python18_10_2020.univer.lesson07.product import Product, ProductException
from datetime import datetime

from ua.python18_10_2020.univer.lesson07.product_list import Product_List

logging.basicConfig(filename="sample.log", level=logging.INFO)
log_prod = logging.getLogger("Product")
log_ex = logging.getLogger("Exception")

def get_3_product():
    products = []
    log_ex.debug("try create 3 product")
    try:
        products.append(Product("apple1", 15, 25))
        products.append(Product("apple2", 10, 20))
        products.append(Product("apple3", 20, 15))
    except ProductException as pe:
        log_prod.error(f"Error {pe}")
        raise pe
    except Exception as e:
        log_ex.error(f"Error {e}")
        raise e
    log_ex.debug("Create 3 product")
    return products

if __name__ == '__main__':
    print(Currency.usd)
    product_list = Product_List(get_3_product())
    product_list.print()
    Currency.usd = 30
    product_list.print()
    
    product_list.get_products_less_value(10)
    product_list.get_max_weight_product()
    product_list.get_sum_price()