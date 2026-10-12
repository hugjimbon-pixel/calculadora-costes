# Calculadora de costes logísticos - Versión 1

# Tarifas (puedes cambiarlas)
TARIFA_BASE = 5.0      # euros fijos por envío
PRECIO_POR_KM = 0.10   # euros por cada km
PRECIO_POR_KG = 0.50   # euros por cada kg

# Pedir datos al usuario
peso = float(input("Peso del envío (kg): "))
distancia = float(input("Distancia (km): "))

# Calcular el coste
coste = TARIFA_BASE + distancia * PRECIO_POR_KM + peso * PRECIO_POR_KG

# Mostrar el resultado
print(f"Coste del envío: {coste:.2f} euros")
