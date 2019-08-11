# Electric appliances class
"""electric Applicances module"""
from inventory_management.inventory_class import Inventory

class ElectricAppliances(Inventory):
    """ Electric Appliances class """
    def __init__(self, product_code, description,
                 market_price,
                 rental_price,
                 brand,
                 voltage):
        super().__init__(product_code, description, market_price,
                         rental_price)
        # Creates common instance variables from the parent class
        self.brand = brand
        self.voltage = voltage

    def return_as_dictionary(self):
        """return the object as a dict"""
        output_dict = Inventory.return_as_dictionary(self)
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage
        return output_dict
