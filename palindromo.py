"""Programa Palindromo"""


def palindromo(texto):
    """Función principal"""

    validacion = False
    texto_alreves = ""
    texto = texto.replace(" ", "")  # Quitar espacios del texto

    # Poner el texto de revés
    for char in texto:
        if char != " ":
            texto_alreves = char + texto_alreves

    # Comprobar si es palindromo
    if texto == texto_alreves:
        validacion = True

    return validacion


print("VERIFICADOR DE PALINDROMO\n")
CONTENIDO_INPUT = input("Ingresa texto a comprobar: ")
print(CONTENIDO_INPUT, ": ", palindromo(CONTENIDO_INPUT))
