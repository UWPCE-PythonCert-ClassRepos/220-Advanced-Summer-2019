"""Furniture class"""
from inventory_management.inventory_class import Inventory


class Furniture(Inventory):
    """
    creates furniture class inheriting from
    Inventory class
    """

    def __init__(self, product_code, description, market_price,
                 rental_price, material, size):
        # Creates common instance variables from the parent class
        Inventory.__init__(self, product_code, description,
                           market_price, rental_price)
        self.material = material
        self.size = size

    def return_as_dictionary(self):
        """
        returns output as dictionary
        """
        output_dict = {}
        output_dict['product_code'] = self.product_code
        output_dict['description'] = self.description
        output_dict['market_price'] = self.market_price
        output_dict['rental_price'] = self.rental_price
        output_dict['material'] = self.material
        output_dict['size'] = self.size

        return output_dict
