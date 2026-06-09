# tests/test_pagos.py
import pytest
from unittest.mock import MagicMock
from app.pagos import ProcesadorPago

# Respuestas a las preguntas de la guía:
# f) ¿Por qué es incorrecto usar la PasarelaPago real en los tests automáticos?
# Es incorrecto porque generaría cobros reales, haría que las pruebas sean lentas y frágiles al depender 
# de la red y de un servicio de terceros que podría no estar disponible.
#
# g) ¿Qué diferencia existe entre un Stub y un Mock? ¿Cuál usaste?
# Un Stub devuelve respuestas predefinidas sin lógica real. Un Mock, además de hacer eso, registra 
# su comportamiento (cuántas veces se llamó y con qué argumentos) para poder hacer aserciones sobre él. 
# En este archivo use un Mock (MagicMock).

@pytest.fixture
def procesador_con_mock():
    """Fixture que provee ProcesadorPago con pasarela mockeada."""
    mock_pasarela = MagicMock()
    mock_pasarela.cobrar.return_value = {"estado": "ok", "txn_id": "TXN-TEST-001"}
    return ProcesadorPago(pasarela=mock_pasarela), mock_pasarela

def test_pago_exitoso_retorna_txn_id(procesador_con_mock):
    procesador, mock_pasarela = procesador_con_mock
    resultado = procesador.procesar(monto=150.0, cliente="ana@mail.com")
    assert resultado["txn_id"] == "TXN-TEST-001"
    assert resultado["estado"] == "ok"

def test_pago_llama_pasarela_con_monto_correcto(procesador_con_mock):
    procesador, mock_pasarela = procesador_con_mock
    procesador.procesar(monto=250.0, cliente="ana@mail.com")
    mock_pasarela.cobrar.assert_called_once_with(monto=250.0)

def test_pago_sin_duplicados(procesador_con_mock):
    """Verifica que no se realizan cobros duplicados."""
    procesador, mock_pasarela = procesador_con_mock
    procesador.procesar(monto=100.0, cliente="juan@mail.com")
    assert mock_pasarela.cobrar.call_count == 1

def test_pago_falla_cuando_pasarela_lanza_excepcion():
    mock_pasarela = MagicMock()
    mock_pasarela.cobrar.side_effect = ConnectionError("Pasarela no disponible")
    procesador = ProcesadorPago(pasarela=mock_pasarela)
    
    with pytest.raises(ConnectionError):
        procesador.procesar(monto=50.0, cliente="luis@mail.com")