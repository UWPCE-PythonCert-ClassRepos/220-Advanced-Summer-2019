# Inventory class
class inventory:

    def __init__(self, productCode, description, marketPrice, rentalPrice):
        self.productCode = productCode
        self.description = description
        self.marketPrice = marketPrice
        self.rentalPrice = rentalPrice

    def returnAsDictionary(self):
        outputDict = {}
        outputDict['productCode'] = self.productCode
        outputDict['description'] = self.description
        outputDict['marketPrice'] = self.marketPrice
        outputDict['rentalPrice'] = self.rentalPrice

        return outputDict