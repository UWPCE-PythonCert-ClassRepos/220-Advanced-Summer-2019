"""Electric appliances class"""
from inventory_class import Inventory


class ElectricAppliances(Inventory):
    """Creates ElectricAppliances Class instance
        with inheritance from the Inventory class"""

    def __init__(self, product_code, description,
                 market_price, rental_price, brand, voltage):
        # Creates common instance variables from the parent class
        Inventory.__init__(self, product_code, description,
                           market_price, rental_price)
        self.brand = brand
        self.voltage = voltage

    def return_as_dictionary(self):
        """Returns info on item as a dictionary"""
        output_dict = Inventory.return_as_dictionary(self)
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage

        return output_dict
