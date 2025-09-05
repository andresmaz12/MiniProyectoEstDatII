from router_hash import RouterHash
import os


def inicializar_rutas_predeterminadas(router):
    # Inicializa el router con rutas predeterminadas
    print("🚀 Inicializando rutas predeterminadas...")
    router.agregar_ruta("192.168.1.1", "eth0")  # hash(...) % 5 = 2
    router.agregar_ruta("10.0.0.2", "eth1")  # hash(...) % 5 = 2 (Colisión)
    router.agregar_ruta("172.16.5.10", "eth2")  # hash(...) % 5 = 4
    router.agregar_ruta("8.8.8.8", "eth3")  # hash(...) % 5 = 2 (Colisión)
    print("\n✅ Rutas predeterminadas cargadas exitosamente!\n")


def limpiar_consola():
    # Para Windows
    if os.name == "nt":
        os.system("cls")
    # Para macOS y Linux
    else:
        os.system("clear")


def presionar_tecla():
    input("\nPresiona Enter para regresar...")


def mostrar_menu():
    # Muestra el menú principal del programa
    print("=" * 50)
    print("SISTEMA DE ENRUTAMIENTO HASH")
    print("=" * 50)
    print("OPCIONES DISPONIBLES:")
    print("1.) Agregar nueva ruta")
    print("2.) Buscar ruta existente")
    print("3.) Mostrar tabla de rutas")
    print("4.) Salir del programa")
    print("=" * 50)


def agregar_nueva_ruta(router):
    # Permite al usuario agregar una nueva ruta de forma interactiva
    limpiar_consola()
    print("AGREGAR NUEVA RUTA")
    print("-" * 25)

    while True:
        ip = input(" Ingresa la dirección IP (formato: xxx.xxx.xxx.xxx): ").strip()
        if ip:
            break
        print(" Por favor, ingresa una dirección IP válida.")

    while True:
        interfaz = input(
            " Ingresa el nombre de la interfaz (ej: eth0, wlan1): "
        ).strip()
        if interfaz:
            break
        print("Por favor, ingresa un nombre de interfaz válido.")

    router.agregar_ruta(ip, interfaz)
    presionar_tecla()


def buscar_ruta_existente(router):
    # Permite al usuario buscar una ruta de forma interactiva
    limpiar_consola()
    print("BUSCAR RUTA")
    print("-" * 15)

    while True:
        ip = input(" Ingresa la dirección IP a buscar: ").strip()
        if ip:
            break
        print("Por favor, ingresa una dirección IP válida.")

    resultado = router.buscar_ruta(ip)
    if resultado:
        print(f"\n Ruta encontrada: {ip} -> {resultado}")
    elif resultado == 0:
        print(f"\n No se encontró la ruta para la IP: {ip}")

    presionar_tecla()


def mostrar_tabla(router):
    # Muestra la tabla de rutas de forma interactiva
    limpiar_consola()
    print("TABLA DE RUTAS")
    print("-" * 20)
    router.imprimir_tabla()
    presionar_tecla()


def main():
    # Función principal que maneja el menú interactivo
    # Inicializar el router con tamaño 5
    router = RouterHash(size=10)

    # Cargar rutas predeterminadas
    inicializar_rutas_predeterminadas(router)

    while True:
        try:
            mostrar_menu()
            opcion = input("Selecciona una opción (1-4): ").strip()

            if opcion == "1":
                agregar_nueva_ruta(router)
            elif opcion == "2":
                buscar_ruta_existente(router)
            elif opcion == "3":
                mostrar_tabla(router)
            elif opcion == "4":
                limpiar_consola()
                print("¡Gracias por usar el Sistema de Enrutamiento Hash!")
                print("¡Hasta luego!")
                break
            else:
                print(
                    "\nOpción inválida. Por favor, selecciona una opción del 1 al 4."
                )
                presionar_tecla()

        except KeyboardInterrupt:
            print("\n\Programa interrumpido por el usuario.")
            print("¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n Error inesperado: {e}")
            input(" Presiona Enter para continuar...")
        limpiar_consola()


if __name__ == "__main__":
    main()
