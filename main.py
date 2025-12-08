from notas import agregar_nota, mostrar_notas, buscar_notas, filtrar_por_etiqueta, filtrar_por_fecha, mostrar_resultados, editar_nota
from archivos import guardar_notas, cargar_notas, autoguardar
from logger import log_error, log_info,log_warning

def pedir_entero(mensaje):
    """
    Pide un numero entero al usuario. Reintenta si hay error.
    
    Args:
        Mensaje (str): Mensaje a mostrar.
    
    Returns:
        int: Numero entero ingresado por el usuario
    """

    while True:
        valor = input(mensaje)

        if valor.strip().isdigit():
            return int(valor)
        
        print("Debes ingresar un numero entero.")
        log_warning(f"Entrada invalida para entero: '{valor}'")

def mostrar_menu():
    print("""
=====================================
     GESTOR PROFESIONAL DE NOTAS
=====================================
1. Agregar nota
2. Mostrar notas
3. Guardar notas
4. Cargar notas
5. Buscar nota
6. Filtrar por etiqueta
7. Filtrar por fecha
8. Editar nota
0. Salir
-------------------------------------      
""")

def main():
    """
    Punto de entrada principal del porgrama.
    Maneja la interaccion con el usuario
    """
    ruta = "notas.json"
    notas = cargar_notas(ruta)

    log_info("Aplicacion iniciada.")

    while True:
            mostrar_menu()
            opcion = input("Elige una opcion: ").strip()

            if opcion == "1":
                texto = input("Texto de la nota: ")
                etiqueta = input("Etiqueta: ")
                agregar_nota(notas, texto, etiqueta)
                autoguardar(notas)

            elif opcion == "2":
                mostrar_notas(notas)

            elif opcion == "3":
                guardar_notas(notas, ruta)
            
            elif opcion == "4":
                notas = cargar_notas(ruta)
                print("Notas cargadas.")
            
            elif opcion == "5":
                texto = input("Texto a buscar: ")
                resultados = buscar_notas(notas, texto)
                mostrar_resultados(resultados)
            
            elif opcion == "6":
                etiqueta = input("Etiqueta: ")
                resultados = filtrar_por_etiqueta(notas, etiqueta)
                mostrar_resultados(resultados)

            elif opcion == "7":
                fecha = input("Fecha (YYY-MM-DD o YYYY): ")
                resultados = filtrar_por_fecha(notas, fecha)
                mostrar_resultados(resultados)
            
            elif opcion == "8":
                indice = pedir_entero("Número de nota a editar: ") - 1
                nuevo_texto = input("Nuevo texto: ")
                nueva_etiqueta = input("Nueva etiqueta (o ENTER para mantener): ")

                if editar_nota(notas, indice, nuevo_texto, nueva_etiqueta):
                    autoguardar(notas, ruta)
            
            elif opcion == "0":
                print("👋 Saliendo...")
                log_info("Aplicacion cerrada por el usuario.")
                break

            else:
                print("Opcion invalida. Intenta nuevamente.")
                log_warning(f"Opcion invalida seleccionada: '{opcion}'")


if __name__ == "__main__":
    main()