from logica.RegistrarNuevoGasto import add_gasto

def Nuevogasto():
    print("""
    =============================================
            Registrar Nuevo Gasto
    =============================================
    Ingrese la información del gasto:
    ingrese 'S' para guardar o 'C' para cancelar.
    =============================================
    """)
fecha=input("ingresar la fecha para el nuevo gasto: ")
gasto=input("1 Monto del gasto: ")
categoria=input("2 Categoría (ej. comida, transporte, entretenimiento, otros): ")
descripcion=input("3 Descripción (opcional): ")

add_gasto(gasto,fecha,categoria,descripcion)

print(f"Gasto con fecha {fecha} agregado correctamente.")

