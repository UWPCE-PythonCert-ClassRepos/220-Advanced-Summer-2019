"""Furniture class"""
from inventory_class import Inventory

class Furniture(Inventory):
    """
    creates an instance of the furniture class with the
    Inventory class used for inheritance
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
        returns information in a dictionary format to be printed
        """
        # Inventory.return_as_dictionary(self)
        output_dict = {}
        output_dict['productCode'] = self.product_code
        output_dict['description'] = self.description
        output_dict['marketPrice'] = self.market_price
        output_dict['rentalPrice'] = self.rental_price
        output_dict['material'] = self.material
        output_dict['size'] = self.size

        return output_dict
