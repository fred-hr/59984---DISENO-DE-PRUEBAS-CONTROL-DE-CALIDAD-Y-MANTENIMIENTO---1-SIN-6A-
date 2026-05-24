
# Ejemplo: Generación automática de casos de prueba
class GeneradorPruebas:
    """
    En esta era se comenzó a usar MODELOS para generar pruebas
    """
    @staticmethod
    def generar_casos_edad(min_edad, max_edad):
        """
        Genera casos de prueba para validación de edad
        usando la técnica de VALORES LÍMITE (veremos más adelante)
        """
        casos = [
            ("Antes del límite inferior", min_edad - 1),
            ("Límite inferior", min_edad),
            ("Dentro del rango", (min_edad + max_edad) // 2),
            ("Límite superior", max_edad),
            ("Después del límite superior", max_edad + 1)
        ]
        return casos

# Función a probar
def validar_edad_votante(edad):
    if not isinstance(edad, int):
        return "❌ Edad debe ser un número entero"
    if edad < 18:
        return "❌ Menor de edad"
    if edad > 120:
        return "❌ Edad inválida"
    return "✅ Puede votar"

# Generar y ejecutar pruebas automáticamente
print("🧪 EJECUCIÓN DE CASOS DE PRUEBA GENERADOS\n")
casos = GeneradorPruebas.generar_casos_edad(18, 120)

for descripcion, edad in casos:
    resultado = validar_edad_votante(edad)
    print(f"{descripcion:30} | Edad: {edad:3} | {resultado}")