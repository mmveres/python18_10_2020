class Product_List:
    def __init__(self, products):
        self.products = products

    def get_products_less_value(self, value):
        products_less_value = []
        for product in self.products:
            if product.price < value:
                products_less_value.append(product)
        return products_less_value

    def get_max_weight_product(self):
        max_weight_product = self.products[0]
        for product in self.products:
            if product.weight > max_weight_product.weight:
                max_weight_product = product
        return max_weight_product

    def get_sum_price(self):
        sum_price = 0
        for product in self.products:
            sum_price += product.price
        return sum_price

    def print(self):
        for product in self.products:
            print(product)

