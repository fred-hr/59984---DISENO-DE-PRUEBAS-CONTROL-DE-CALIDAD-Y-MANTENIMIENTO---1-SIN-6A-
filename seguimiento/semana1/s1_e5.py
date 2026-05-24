# Ejemplo conceptual: Predicción de áreas propensas a defectos
class PrediccionDefectos:
    """
    En la era moderna, se usa ML para predecir qué código tiene mayor
    probabilidad de contener defectos
    """
    
    @staticmethod
    def calcular_riesgo(complejidad, cambios_recientes, cobertura_pruebas):
        """
        Factores que predicen defectos:
        - Complejidad ciclomática alta
        - Muchos cambios recientes
        - Baja cobertura de pruebas
        """
        # Fórmula simplificada (en realidad se usa ML)        
        riesgo = (complejidad * 0.4 + 
                    cambios_recientes * 0.3 +  
                    (100 - cobertura_pruebas) * 0.3)
        
        if riesgo > 70:
            return "🔴 RIESGO CRÍTICO - Priorizar testing"
        elif riesgo > 40:
            return "🟡 RIESGO MEDIO - Aumentar cobertura"
        else:
            return "🟢 RIESGO BAJO - Mantener vigilancia"

# Análisis de módulos
modulos = [
    {"nombre": "Login", "complejidad": 15, "cambios": 3, "cobertura": 85},
    {"nombre": "Pago", "complejidad": 45, "cambios": 12, "cobertura": 60},
    {"nombre": "Reporte", "complejidad": 30, "cambios": 25, "cobertura": 40}
]

print("🎯 PREDICCIÓN DE RIESGOS\n")
for modulo in modulos:
    riesgo = PrediccionDefectos.calcular_riesgo(
        modulo["complejidad"],
        modulo["cambios"],
        modulo["cobertura"]
    )
    print(f"{modulo['nombre']:15} | {riesgo}")