"""
electric_appliances module
"""

from inventory import Inventory


class ElectricAppliances(Inventory):
    """
    ElectricAppliances class
    """

    def __init__(self, product_code, description, market_price, rental_price, brand, voltage):
        """

        :param product_code:
        :param description:
        :param market_price:
        :param rental_price:
        :param brand:
        :param voltage:
        """
        Inventory.__init__(self, product_code, description, market_price, rental_price)
        # Creates common instance variables from the parent class

        self.brand = brand
        self.voltage = voltage

    def return_as_dictionary(self):
        """

        :return:
        """
        output_dict = {}
        output_dict['product_code'] = self.product_code
        output_dict['description'] = self.description
        output_dict['market_price'] = self.market_price
        output_dict['rental_price'] = self.rental_price
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage

        return output_dict
