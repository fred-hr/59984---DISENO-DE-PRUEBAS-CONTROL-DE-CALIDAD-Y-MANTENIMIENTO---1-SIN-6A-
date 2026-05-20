from pyDOE3 import ff2n
import pandas as pd

# Generar diseño factorial 2^3 (3 factores binarios)
diseño = ff2n(3)
df = pd.DataFrame(diseño, columns=["Temperatura", "Tiempo", "Rejilla"])
print(df)