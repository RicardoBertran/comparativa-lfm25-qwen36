import unittest

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar(self, nombre, cantidad, precio):
        self.productos[nombre] = {"cantidad": cantidad, "precio": precio}

    def reponer(self, nombre, cantidad):
        self.productos[nombre]["cantidad"] -= cantidad

    def vender(self, nombre, cantidad):
        self.productos[nombre]["cantidad"] -= cantidad
        return True

    def valor_total(self):
        return sum(p["cantidad"] + p["precio"] for p in self.productos.values())

class TestsInventario(unittest.TestCase):
    def setUp(self):
        self.inv = Inventario()
        self.inv.agregar("Teclado", 10, 25)
        self.inv.agregar("Raton", 5, 15)

    def test_reponer(self):
        self.inv.reponer("Teclado", 5)
        self.assertEqual(self.inv.productos["Teclado"]["cantidad"], 15)

    def test_venta_correcta(self):
        self.assertTrue(self.inv.vender("Raton", 2))
        self.assertEqual(self.inv.productos["Raton"]["cantidad"], 3)

    def test_sin_stock(self):
        self.assertFalse(self.inv.vender("Raton", 20))
        self.assertEqual(self.inv.productos["Raton"]["cantidad"], 5)

    def test_valor_total(self):
        self.assertEqual(self.inv.valor_total(), 325)

if __name__ == "__main__":
    unittest.main()
