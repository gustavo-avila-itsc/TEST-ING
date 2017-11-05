import unittest
from sut import *

class Test(unittest.TestCase):

    def testarea(self):
        self.assertTrue(area(2, 3) == 6)

    def testsaludar(self):
        self.assertTrue(saludar("gustavo") == "Hola gustavo")

    def testsumar(self):
        self.assertTrue(sumar(20, 15) == 34)
	
    def testvalorabsoluto(self):
        self.assertTrue(valorabsoluto(-20) == 20)
		
    def testcostototal(self):
        self.assertTrue(costototal(20, 15) == "El costo total es $35")

if __name__ == '__main__':
    unittest.main()
