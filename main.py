from router_hash import RouterHash

router = RouterHash(size=5)

print("1. Agregando rutas iniciales...")
# Agregando las rutas del ejemplo del documento
router.agregar_ruta("192.168.1.1", "eth0")  # hash(...) % 5 = 2
router.agregar_ruta("10.0.0.2", "eth1")  # hash(...) % 5 = 2 (Colisión)
router.agregar_ruta("172.16.5.10", "eth2")  # hash(...) % 5 = 4
router.agregar_ruta("8.8.8.8", "eth3")  # hash(...) % 5 = 2 (Colisión)

# Mostramos el estado de la tabla
router.imprimir_tabla()

# Buscando rutas de ejemplo
print("2. Simulando llegada de paquetes (búsqueda de rutas)...")
paquetes = ["192.168.1.1", "10.0.0.2", "8.8.8.8", "192.168.0.100"]
for ip in paquetes:
    interfaz = router.buscar_ruta(ip)
    print(f"Paquete para {ip} -> Enviando a la interfaz: {interfaz}")
