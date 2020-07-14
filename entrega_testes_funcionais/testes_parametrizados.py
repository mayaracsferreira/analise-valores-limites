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
dias =      [0, 1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 29, 30, 31 ]
esperado = [-1, 450.0, 450.0, 450.0, 450.0, 475.0, 475.0, 475.0, 475.0, 500.0, 500.0, 500.0, 500.0, 510.5, 511.0, 517.0, 517.5, -1]
cenarios = []
resultados = []

### Coletando dados da API
for index, dia in enumerate(dias):
    aluguel = Aluguel(VALOR_NOMINAL, dia)
    resultado = aluguel.calcula_valor()
    resultados.append(resultado['valor_calculado'])    
    cenarios.append((dias[index],esperado[index], resultado['valor_calculado']))

### Parametrizando os testes
@pytest.mark.parametrize('dia, esperado,atual', cenarios)
def test_cenarios(dia, esperado, atual):
    sys.stderr.write("Dia: {} Esperado {} recebido {}".format(dia, esperado, atual))
    assert atual == esperado
