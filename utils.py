import unittest
from utils import somar, subtrair, multiplicar, dividir

class TestUtilidadesGerais(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(10, 5), 15)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(-1, -1), -2)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(-1, 1), -2)
        self.assertEqual(subtrair(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(10, 5), 50)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(-1, 1), -1)
        self.assertEqual(dividir(-1, -1), 1)
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == '__main__':
    unittest.main()
