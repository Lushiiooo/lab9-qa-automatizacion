#Respuesta laboratorio 9

## Tarea 04: Cobertura de Código con pytest-cov

**k) ¿Qué líneas quedaron sin cubrir al ejecutar el primer reporte? ¿Por qué?**
Según el reporte, quedaron sin cubrir la línea 12 en `app/carrito.py` y la línea 19 en `app/pagos.py`. Estas líneas corresponden a las sentencias `raise ValueError` que se activan al ingresar un precio negativo en el carrito y un monto negativo en los pagos. Como las pruebas unitarias no incluyeron escenarios que enviaran números negativos a estas funciones específicas, el intérprete nunca ejecutó esas líneas.

**l) ¿Significa cobertura 100% que el software no tiene bugs? Justifica con un ejemplo concreto del laboratorio.**
No. La cobertura del 100% únicamente certifica que todas las líneas de código fueron ejecutadas durante las pruebas, pero no garantiza que la lógica de negocio sea correcta. Un ejemplo claro fue el módulo `app/descuentos.py`. Podría haber obtenido un 100% de cobertura ejecutando un solo test básico, pero el código original contenía un bug matemático crítico (multiplicaba en vez de restar el descuento). Si el test no validaba el resultado matemático exacto, el bug habría llegado a producción a pesar de tener cobertura total.



## Tarea 05: Gestión de Defectos

**o) ¿Cuál fue la severidad que asignaste a cada bug? Justifica tu decisión.**
Asigné una severidad ALTA (HIGH) al bug de la fórmula matemática en los descuentos. Mi justificación es que el cálculo de precios es una funcionalidad core del sistema; si se cobra mal, hay un impacto financiero directo, aunque el sistema como tal no sufra una caída total (lo que sería un nivel CRITICAL).

**p) ¿En qué se diferencia la severidad de la prioridad? Da un ejemplo donde ambas sean distintas.**
La **severidad** mide el impacto técnico del defecto (qué tanto "rompe" el sistema o impide su uso). La **prioridad** mide la urgencia de negocio (qué tan rápido debe ser solucionado por el equipo). 
*Ejemplo donde son distintas:* Un error ortográfico grave en el título principal de la página de inicio. Su severidad es BAJA (no afecta la funcionalidad, el código se ejecuta perfecto), pero su prioridad es ALTA (daña la imagen de la empresa y los directivos exigen que se corrija inmediatamente).