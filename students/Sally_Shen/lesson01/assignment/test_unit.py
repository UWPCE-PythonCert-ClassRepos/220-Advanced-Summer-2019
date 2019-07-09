pass
import unittest

class demo(unittest,TestCase):
    productCode = "A1234"
    #inventory =
    def test_demo(self):
        self.assertDictEqual({"productCode" : "A1234"}, {"productCode": "A1234"})