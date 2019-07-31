from inventory_management.inventory_class import Inventory


class Furniture(Inventory):
    """ This class handles the Furniture Object """

    def __init__(self, product_code, description, market_price, rental_price,
                 material, style):
        # Creates common instance variables from the parent class
        self.material = material
        self.style = style
        super().__init__(product_code, description, market_price, rental_price)

    def return_as_dictionary(self):
        """ This returns a dictionary containing the expected fields """
        output_dict = super().return_as_dictionary()
        output_dict['material'] = self.material
        output_dict['style'] = self.style

        return output_dict