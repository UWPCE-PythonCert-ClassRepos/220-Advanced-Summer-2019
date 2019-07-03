# Furniture class
""" Furniture module """
from inventoryClass import Inventory

class Furniture(Inventory):
    """ Furniture class, inherits Inventory class """
    def __init__(self,
                 productCode,
                 description,
                 marketPrice,
                 rentalPrice,
                 material,
                 size):
        Inventory.__init__(self,
                           productCode,
                           description,
                           marketPrice,
                           rentalPrice) # Creates common instance variables from the parent class

        self.material = material
        self.size = size

    def return_as_dictionary(self):
        output_dict = {}
        output_dict['productCode'] = self.product_code
        output_dict['description'] = self.description
        output_dict['marketPrice'] = self.market_price
        output_dict['rentalPrice'] = self.rental_price
        output_dict['material'] = self.material
        output_dict['size'] = self.size

        return output_dict
