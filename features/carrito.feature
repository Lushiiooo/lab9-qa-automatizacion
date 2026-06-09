# features/carrito.feature

Feature: Gestión del carrito de compras
  Como cliente registrado de la tienda
  Quiero administrar los productos de mi carrito
  Para completar mi compra de forma eficiente

  Background:
    Given tengo un carrito vacio

  Scenario: Agregar un producto al carrito
    When agrego el producto "Laptop" con precio 800 y cantidad 1
    Then el carrito tiene 1 articulo
    And el total del carrito es 800

  Scenario: Agregar múltiples productos distintos
    When agrego el producto "Monitor" con precio 300 y cantidad 2
    And agrego el producto "Teclado" con precio 80 y cantidad 1
    Then el carrito tiene 3 articulos
    And el total del carrito es 680

  # Escenario completado (Tarea 3, paso 3)
  Scenario: Vaciar el carrito
    When agrego el producto "Monitor" con precio 300 y cantidad 2
    And vacio el carrito
    Then el carrito tiene 0 articulos
    And el total del carrito es 0

  Scenario Outline: Aplicar descuento por volumen
    When agrego el producto "Monitor" con precio 300 y cantidad <cantidad>
    And aplico el codigo de descuento "<codigo>"
    Then el total con descuento es <total_final>

    Examples:
      | cantidad | codigo  | total_final |
      | 1        | PROMO10 | 270         |
      | 2        | PROMO20 | 480         |