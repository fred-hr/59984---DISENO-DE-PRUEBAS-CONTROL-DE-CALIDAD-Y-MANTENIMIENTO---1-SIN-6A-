import numpy as np

def varianza(datos):
    return np.var(datos)

# Relación metamórfica: sumar una constante no cambia la varianza
def test_varianza_metamorfica():
    datos = np.array([1, 2, 3, 4, 5])
    salida1 = varianza(datos)
    salida2 = varianza(datos + 10)
    assert np.isclose(salida1, salida2)