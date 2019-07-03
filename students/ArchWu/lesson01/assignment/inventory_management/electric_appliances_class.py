# Electric appliances class
"""electric Applicances module"""
from inventoryClass import Inventory

class ElectricAppliances(Inventory):
    """ Electric Appliances class """
    def __init__(self,
                 productCode,
                 description,
                 marketPrice,
                 rentalPrice,
                 brand,
                 voltage):
        Inventory.__init__(self,
                           productCode,
                           description,
                           marketPrice,
                           rentalPrice)
        # Creates common instance variables from the parent class


        self.brand = brand
        self.voltage = voltage

    def return_as_dictionary(self):
        output_dict = {}
        output_dict['productCode'] = self.product_code
        output_dict['description'] = self.description
        output_dict['marketPrice'] = self.market_price
        output_dict['rentalPrice'] = self.rental_price
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage

        return output_dict
