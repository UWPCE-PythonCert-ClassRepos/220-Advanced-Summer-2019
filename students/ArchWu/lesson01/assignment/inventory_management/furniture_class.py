# Furniture class
""" Furniture module """
from inventory_class import Inventory

class Furniture(Inventory):
    """ Furniture class, inherits Inventory class """
    def __init__(self,
                 productCode,
                 description,
                 marketPrice,
                 rentalPrice,
                 material,
                 size):
        super().__init__(productCode,
                         description,
                         marketPrice,
                         rentalPrice)
        # Creates common instance variables from the parent class
        self.material = material
        self.size = size

    def return_as_dictionary(self):
        output_dict = Inventory.return_as_dictionary(self)
        output_dict['material'] = self.material
        output_dict['size'] = self.size
        return output_dict
