#Respuesta laboratorio 9

## Tarea 04: Cobertura de Código con pytest-cov

**k) ¿Qué líneas quedaron sin cubrir al ejecutar el primer reporte? ¿Por qué?**
Según el reporte, quedaron sin cubrir la línea 12 en `app/carrito.py` y la línea 19 en `app/pagos.py`. Estas líneas corresponden a las sentencias `raise ValueError` que se activan al ingresar un precio negativo en el carrito y un monto negativo en los pagos. Como las pruebas unitarias no incluyeron escenarios que enviaran números negativos a estas funciones específicas, el intérprete nunca ejecutó esas líneas.

**l) ¿Significa cobertura 100% que el software no tiene bugs? Justifica con un ejemplo concreto del laboratorio.**
No. La cobertura del 100% únicamente certifica que todas las líneas de código fueron ejecutadas durante las pruebas, pero no garantiza que la lógica de negocio sea correcta. Un ejemplo claro fue el módulo `app/descuentos.py`. Podría haber obtenido un 100% de cobertura ejecutando un solo test básico, pero el código original contenía un bug matemático crítico (multiplicaba en vez de restar el descuento). Si el test no validaba el resultado matemático exacto, el bug habría llegado a producción a pesar de tener cobertura total.