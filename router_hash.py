class RouterHash:
    def __init__(self, size):
        # Inicializa la tabla hash con un tamaño fijo y la llena con None que representa ratunas vacías.
        self.size = size
        self.tabla = [None] * size

    def ip_a_entero(self, ip):
        # Convierte una dirección IP en formato de cadena a un entero de 32 bits
        try:
            resultado = 0
            octetos = ip.split(".")
            if len(octetos) != 4:
                raise ValueError("\n(*) Error: La dirección ip debe tener 4 octetos.")
            for i, octeto in enumerate(octetos):
                octeto_int = int(octeto)
                if octeto_int < 0 or octeto_int > 255:
                    raise ValueError(
                        "\n(*) Error: La dirección ip debe estar entre 0 y 255."
                    )

                # Desplazamiento: 24, 16, 8, 0 bits
                resultado += octeto_int << (24 - i * 8)

            return resultado

        except (ValueError, IndexError):
            print("\n(*) Error: La dirección ip no es válida.")
            return None

    def funcion_hash(self, ip):
        # Calcula el hash de una IP y retorna el índice
        h = ip % self.size
        return h

    def agregar_ruta(self, ip, interfaz):
        # Agrega una ruta utilizando sondeo lineal para resolver colisiones
        ip_int = self.ip_a_entero(ip)

        if ip_int is None:
            return

        indice = self.funcion_hash(ip_int)
        indice_original = indice

        while self.tabla[indice] is not None:
            # Si la IP ya existe, se actualiza la interfaz y se termina.
            if self.tabla[indice][0] == ip:
                print(f"\nRuta actualizada: {ip} -> {interfaz}")
                self.tabla[indice] = (ip, interfaz)
                return

            # Sondeo lineal: se pasa al siguiente índice.
            indice = (indice + 1) % self.size
            # Si se ha vuelto al inicio, la tabla está llena.
            if indice == indice_original:
                print("\n(*) Error: La tabla de enrutamiento esta llena.")
                return

        # Se encuentra una ranura vacía y se inserta la nueva ruta.
        self.tabla[indice] = (ip, interfaz)
        print(f"\nRuta agregada: {ip} -> {interfaz} en el indice {indice}")

    def buscar_ruta(self, ip):
        # Busca la interfaz de salida para una dirección IP de destino.
        ip_int = self.ip_a_entero(ip)

        if ip_int is None:
            return

        indice = self.funcion_hash(ip_int)
        indice_original = indice

        while self.tabla[indice] is not None:
            # Si se encuentra la IP, se devuelve la interfaz asociada.
            if self.tabla[indice][0] == ip:
                return self.tabla[indice][1]

            # Sondeo lineal: se pasa al siguiente índice.
            indice = (indice + 1) % self.size
            # Si se ha vuelto al inicio sin encontrarla, la ruta no existe.
            if indice == indice_original:
                break

        return 0

    def imprimir_tabla(self):
        # Funcion  para visualizar la tabla de rutas
        for i, item in enumerate(self.tabla):
            if item is None:
                print(f"Índice {i}: [Vacío]")
            else:
                print(f"Índice {i}: IP: {item[0]} -> Interfaz: {item[1]}")
        print("----------------------------------\n")
