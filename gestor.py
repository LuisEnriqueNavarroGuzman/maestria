# Gestor de decisión para concesión de crédito

# Definición de variables
nombre = "Luis Enrique"
edad = 30
ingresos_mensuales = 25000
gastos_mensuales = 10000
dependientes = 2
historial_bueno = True
antiguedad_laboral = 4

# Operador aritmético
capacidad_pago = ingresos_mensuales - gastos_mensuales

print("Solicitante:", nombre)
print("Capacidad de pago:", capacidad_pago)

# Decisión principal:
# Se aprueba si es mayor de edad, tiene historial bueno,
# capacidad de pago mayor a 12,000 y antigüedad laboral mínima de 2 años.
if edad >= 18 and historial_bueno and capacidad_pago > 12000 and antiguedad_laboral >= 2:
    print("Crédito aprobado")

# Si no cumple todas las condiciones anteriores,
# pero tiene capacidad de pago mayor a 8,000 y máximo 3 dependientes,
# entonces el crédito queda en revisión.
elif capacidad_pago > 8000 and dependientes <= 3:
    print("Solicitud en revisión")

# Si no cumple ninguna de las condiciones anteriores,
# el crédito es rechazado.
else:
    print("Crédito rechazado")