# Test-Driven Development (TDD) - ¡Pruebas ANTES del código!

import unittest

class TestCalculadora(unittest.TestCase):
    """
    En TDD: Escribimos la prueba PRIMERO (y falla)
    Luego escribimos el código mínimo para que pase
    """
    def test_suma_numeros_positivos(self):
        # 1. RED: La prueba falla porque la función no existe
        self.assertEqual(suma(2, 3), 5)
    
    def test_suma_con_cero(self):
        self.assertEqual(suma(5, 0), 5)

    def test_suma_numeros_negativos(self):
        self.assertEqual(suma(-2, -3), -5)

# 2. GREEN: Escribimos el código mínimo
def suma(a, b):
    return a + b

# 3. REFACTOR: Mejoramos el código (si es necesario)

if __name__ == '__main__':
    unittest.main()