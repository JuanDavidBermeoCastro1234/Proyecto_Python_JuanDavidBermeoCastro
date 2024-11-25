from logica.RegistrarNuevoGasto import read_file,write_file,add_gasto

def Nuevogasto():
    print("""
    =============================================
            Registrar Nuevo Gasto
    =============================================
    Ingrese la información del gasto:
    ingrese 'S' para guardar o 'C' para cancelar.
    =============================================
    """)

id=input("ingresar id para el nuevo gasto")
gasto=input("1 Monto del gasto:")
categoria=input("2 Categoría (ej. comida, transporte, entretenimiento, otros):")
descripcion=input("3 Descripción (opcional):")

add_gasto(gasto,id,categoria,descripcion)