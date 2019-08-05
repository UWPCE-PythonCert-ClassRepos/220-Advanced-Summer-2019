"""Furniture class"""
from inventory_management.inventory_class import Inventory

class Furniture(Inventory):
    """
        Creates furniture class which inherit from
        Inventory class
    """
    def __init__(self, product_code, description,
                 market_price, rental_price, material, size):
        # Creates common instance variables from the parent class
        Inventory.__init__(self, product_code, description,
                           market_price, rental_price)

        self.material = material
        self.size = size

    def return_as_dictionary(self):
        """
        Returns output as dictionary
        """
        output_dict = super().return_as_dictionary()
        output_dict['material'] = self.material
        output_dict['size'] = self.size

        return output_dict
        