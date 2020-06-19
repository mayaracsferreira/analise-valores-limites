import json
import os
import sys
import inspect
currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from Aluguel import Aluguel

VALOR_NOMINAL = 500.0


def test_dia_maior_que_30_MCSF():
    aluguel = Aluguel(VALOR_NOMINAL, 31)
    valor = aluguel.calcula_valor()
    assert valor['valor_calculado'] == -1


def test_dia_menor_que_0_MCSF():
    aluguel = Aluguel(VALOR_NOMINAL, -1)
    valor = aluguel.calcula_valor()
    assert valor['valor_calculado'] == -1


def test_dia_1_MCSF():
    aluguel = Aluguel(VALOR_NOMINAL, 1)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.1
    assert valor['valor_calculado'] == valor_aluguel


def test_dia_6_MCSF():
    aluguel = Aluguel(VALOR_NOMINAL, 6)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.05
    assert valor['valor_calculado'] == valor_aluguel


def test_dia_11_MCSF():
    aluguel = Aluguel(VALOR_NOMINAL, 11)
    valor = aluguel.calcula_valor()
    assert valor['valor_calculado'] == aluguel.valor_nominal