""" Inventory class """


class Inventory:
    """
    This class manages product codes, descriptions and pricing
    """

    def __init__(self, product_code, description, market_price, rental_price):
        self.product_code = product_code
        self.description = description
        self.market_price = market_price
        self.rental_price = rental_price

    def return_as_dictionary(self):
        """
        Provides inventory data
        :return: dictionary
        """
        return self.__dict__
