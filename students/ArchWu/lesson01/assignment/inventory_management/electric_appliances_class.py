# Electric appliances class
"""electric Applicances module"""
from inventory_class import Inventory

class ElectricAppliances(Inventory):
    """ Electric Appliances class """
    def __init__(self, productCode, description,
                 marketPrice,
                 rentalPrice,
                 brand,
                 voltage):
        super().__init__(self, productCode, description, marketPrice,
                         rentalPrice)
        # Creates common instance variables from the parent class
        self.brand = brand
        self.voltage = voltage

    def return_as_dictionary(self):
        output_dict = Inventory.return_as_dictionary(self)
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage
        return output_dict
