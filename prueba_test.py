import unittest
from sut import *

class Test(unittest.TestCase):

    def testarea(self):
        self.assertEqual(area(2, 3),6)

    def testsaludar(self):
        self.assertEqual(saludar("gustavo"),"Hola gustavo")

    def testsumar(self):
        self.assertEqual(sumar(20, 15),35)

    def testcomparar(self):
        self.assertEqual(comparar(3,5),"A menor que B")
    def testcomparar2(self):
        self.assertEqual(comparar(5,3),"A mayor que B")
    def testcomparar3(self):
        self.assertEqual(comparar(5,5),"A y B son iguales")


	
    def testvalorabsoluto(self):
        self.assertEqual(valorabsoluto(-20),20)
        
    def testvalorabsoluto2(self):
        self.assertEqual(valorabsoluto(20),20)
        
    def testcostototal(self):
        self.assertEqual(costototal(20, 15),"El costo total es $35")
if __name__ == '__main__':
    unittest.main()
