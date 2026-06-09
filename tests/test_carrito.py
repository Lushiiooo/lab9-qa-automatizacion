# tests/test_carrito.py

# Nota: No es necesario importar 'carrito_vacio', pytest lo inyecta automáticamente desde conftest.py

def test_agregar_producto_incrementa_cantidad(carrito_vacio):
    """Agrega 1 producto y verifica que cantidad() == 1."""
    carrito_vacio.agregar("Laptop", 800)
    assert carrito_vacio.cantidad() == 1

def test_carrito_vacio_al_iniciar(carrito_vacio):
    """Verifica que un carrito recién creado tiene 0 items."""
    assert carrito_vacio.cantidad() == 0

def test_total_suma_precios_correctamente(carrito_vacio):
    """Agrega 2 productos y verifica que total() retorna la suma correcta."""
    carrito_vacio.agregar("Laptop", 800)
    carrito_vacio.agregar("Teclado", 80)
    assert carrito_vacio.total() == 880

def test_agregar_producto_duplicado_incrementa_cantidad(carrito_vacio):
    """Agrega el mismo producto dos veces y verifica cantidad == 2."""
    carrito_vacio.agregar("Laptop", 800)
    carrito_vacio.agregar("Laptop", 800)
    assert carrito_vacio.cantidad() == 2

def test_vaciar_deja_carrito_en_cero(carrito_vacio):
    """Agrega productos, llama vaciar() y verifica que cantidad() == 0."""
    carrito_vacio.agregar("Monitor", 300)
    carrito_vacio.vaciar()
    assert carrito_vacio.cantidad() == 0