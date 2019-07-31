"""this class inherits class inventory"""
from inventory_management.inventory_class import Inventory


class Furniture(Inventory):
    """Furniture Class"""
    def __init__(self, product_code, description, market_price, rental_price,
                 material, size):
        # Creates common instance variables from the parent class
        self.material = material
        self.size = size
        super().__init__(product_code, description, market_price, rental_price)

    def return_as_dictionary(self):
        """ This returns a dictionary containing the expected fields """
        output_dict = super().return_as_dictionary()
        output_dict['material'] = self.material
        output_dict['size'] = self.size

        return output_dict
