import unittest
from estructuras import CadenaInvertida


class TestCadenaInvertida():

    def test_cadena_invertida(self):
        self.assertEqual(CadenaInvertida("Python"), "ntyP")


if __name__ == '__main__':
    unittest.main()
