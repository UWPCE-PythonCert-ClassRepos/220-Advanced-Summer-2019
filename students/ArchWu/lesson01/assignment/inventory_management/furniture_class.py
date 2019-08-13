# Furniture class
""" Furniture module """
from inventory_management.inventory_class import Inventory

class Furniture(Inventory):
    """ Furniture class, inherits Inventory class """
    def __init__(self,
                 product_code,
                 description,
                 market_price,
                 rental_price,
                 material,
                 size):
        super().__init__(product_code,
                         description,
                         market_price,
                         rental_price)
        # Creates common instance variables from the parent class
        self.material = material
        self.size = size

    def return_as_dictionary(self):
        """return the object as a dict"""
        output_dict = Inventory.return_as_dictionary(self)
        output_dict['material'] = self.material
        output_dict['size'] = self.size
        return output_dict
