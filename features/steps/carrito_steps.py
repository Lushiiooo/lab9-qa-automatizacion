# features/steps/carrito_steps.py
from behave import given, when, then
from app.carrito import Carrito
from app.descuentos import calcular_descuento

@given('tengo un carrito vacio')
def step_carrito_vacio(context):
    context.carrito = Carrito()

@when('agrego el producto "{nombre}" con precio {precio:d} y cantidad {cantidad:d}')
def step_agregar_producto(context, nombre, precio, cantidad):
    for _ in range(cantidad):
        context.carrito.agregar(nombre, precio)

@when('vacio el carrito')
def step_vaciar_carrito(context):
    context.carrito.vaciar()

@when('aplico el codigo de descuento "{codigo}"')
def step_aplicar_descuento(context, codigo):
    context.codigo_descuento = codigo

@then('el carrito tiene {cantidad:d} {palabra}')
def step_verificar_cantidad(context, cantidad, palabra):
    # La variable "palabra" absorbe "articulo" o "articulos" para reutilizar la función
    assert context.carrito.cantidad() == cantidad, \
        f"Esperado: {cantidad}, Obtenido: {context.carrito.cantidad()}"

@then('el total del carrito es {total:d}')
def step_verificar_total(context, total):
    assert context.carrito.total() == total, \
        f"Esperado: {total}, Obtenido: {context.carrito.total()}"

@then('el total con descuento es {total_final:d}')
def step_verificar_total_descuento(context, total_final):
    total_actual = context.carrito.total()
    # Obtenemos el código guardado en el paso anterior, o string vacío si no existe
    codigo = getattr(context, 'codigo_descuento', '')
    total_calculado = calcular_descuento(total_actual, codigo)
    
    assert total_calculado == total_final, \
        f"Esperado: {total_final}, Obtenido: {total_calculado}"