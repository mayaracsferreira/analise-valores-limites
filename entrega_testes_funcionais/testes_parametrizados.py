from Aluguel import Aluguel
import pandas as pd
import pytest
import sys
import os
import inspect
currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

VALOR_NOMINAL = 500.0
CENARIOS = [(0, -1), (1, 450.0), (2, 450.0), (4, 450.0), (5, 450.0), (6, 475.0), (7, 475.0), (9, 475.0), (10, 475.0), (11, 500.0), (12, 500.0), (14, 500.0), (15, 500.0), (16, 510.5), (17, 511.0), (29, 517.0), (30, 517.5), (31, -1)]

### Parametrizando os testes
@pytest.mark.parametrize('dia, esperado', CENARIOS)
def test_cenarios(dia, esperado):
    aluguel = Aluguel(VALOR_NOMINAL, dia)
    resultado = aluguel.calcula_valor()
    atual = resultado['valor_calculado']
    sys.stderr.write("Dia: {} Esperado {} recebido {}".format(dia, esperado, atual))
    assert atual == esperado
