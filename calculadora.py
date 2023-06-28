"""Calculadora"""

OPERADORES = ["suma", "resta", "multi", "div", "salir"]


def calculadora():
    """Función principal de la app"""

    print("""
    BIENVENIDOS A CALCULADORA
    Para salir ingrese: SALIR.
    Para Operaciones: SUMA, MULTI, RESTA y DIV.
    """)

    entrada_numero_uno = None
    while True:

        # Entrada de Primer Numero y Validación
        if entrada_numero_uno is None:
            entrada_numero_uno = input("Ingresa un numero: ")
            if entrada_numero_uno.lower().strip() == "salir":
                break

            try:
                entrada_numero_uno = float(entrada_numero_uno)
            except ValueError:
                print("Ingrese un numero valido")
                entrada_numero_uno = None
                continue

        # Entrada de Operador y Validación
        entrada_operador = input("Ingresa operador: ")
        if not entrada_operador.lower().strip() in OPERADORES:
            print("El operador no es valido, intentelo de nuevo.")
            continue
        if entrada_operador.lower().strip() == "salir":
            break

        # Entrada de Segundo Numero y Validación
        entrada_numero_dos = input("Ingresa siguiente numero: ")
        if entrada_numero_dos.lower().strip() == "salir":
            break
        else:
            while True:
                try:
                    entrada_numero_dos = float(entrada_numero_dos)
                    break
                except ValueError:
                    print("Ingrese un numero valido")
                    entrada_numero_dos = input("Ingresa siguiente numero: ")

        # Operación Final de Ciclo y resultado
        if entrada_operador.lower().strip() == "suma":
            entrada_numero_uno += entrada_numero_dos
        elif entrada_operador.lower().strip() == "resta":
            entrada_numero_uno -= entrada_numero_dos
        elif entrada_operador.lower().strip() == "multi":
            entrada_numero_uno *= entrada_numero_dos
        elif entrada_operador.lower().strip() == "div":
            entrada_numero_uno /= entrada_numero_dos

        print("Resultado:", round(entrada_numero_uno, 2))


calculadora()
