#----------------------Enunciado--------------------------
#Pide un nombre por pantalla, averigua su longitud con len(), y muestra el resultado de la
#siguiente forma: “Hola <nombre_dado>, tu nombre tiene <longitud> letras.”

def main():
    while True:
        us_name = input("Ingrese tu nombre de usuario (escribe 'salir' para terminar): ")

        if us_name.lower() == "salir":
            print("Cerrando el programa.")
            break
        else:
            user_input = us_name.lower()
            nom = user_input.capitalize()
            long = len(us_name)
            print("Hola {}, tu nombre tiene {} letras.".format(nom, long))

if __name__ == "__main__":
    main()