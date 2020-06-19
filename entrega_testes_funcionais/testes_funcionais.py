import json
import os
import sys
import inspect
currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from Aluguel import Aluguel
import logging

VALOR_NOMINAL = 500.0
log = logging.getLogger()
handler = logging.StreamHandler()
log.addHandler(handler)


def test_dia_menor_que_0_MCSF():
    aluguel = Aluguel(VALOR_NOMINAL, -1)
    valor = aluguel.calcula_valor()    
    sys.stderr.write("Esperado {} recebido {}".format(
        -1, valor['valor_calculado']))
    assert valor['valor_calculado'] == -1

def test_dia_1_MCSF():
    aluguel = Aluguel(VALOR_NOMINAL, 1)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.1    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel

def test_dia_5_MCSF():
    aluguel = Aluguel(VALOR_NOMINAL, 5)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.1    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel


def test_dia_6_MCSF():
    aluguel = Aluguel(VALOR_NOMINAL, 6)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.05    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel

def test_dia_10_MCSF():
    aluguel = Aluguel(VALOR_NOMINAL, 10)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.05    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel

def test_dia_11_MCSF():
    aluguel = Aluguel(VALOR_NOMINAL, 11)
    valor = aluguel.calcula_valor()    
    sys.stderr.write("Esperado {} recebido {}".format(
        aluguel.valor_nominal, valor['valor_calculado']))
    assert valor['valor_calculado'] == aluguel.valor_nominal

def test_dia_15_MCSF():
    DIA = 15
    aluguel = Aluguel(VALOR_NOMINAL, DIA)
    valor = aluguel.calcula_valor()
    multa = aluguel.valor_nominal * 0.02
    dias_atraso = DIA - 15 
    multa_p_dia = aluguel.valor_nominal * 0.001 * dias_atraso
    valor_multas = aluguel.valor_nominal + multa + multa_p_dia
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_multas, valor['valor_calculado']))
    assert valor['valor_calculado'] != valor_multas

def test_dia_16_MCSF():
    DIA = 16
    aluguel = Aluguel(VALOR_NOMINAL, DIA)
    valor = aluguel.calcula_valor()
    multa = aluguel.valor_nominal * 0.02
    dias_atraso = DIA - 15 
    multa_p_dia = aluguel.valor_nominal * 0.001 * dias_atraso
    valor_multas = aluguel.valor_nominal + multa + multa_p_dia
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_multas, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_multas

def test_dia_30_MCSF():
    DIA = 30
    aluguel = Aluguel(VALOR_NOMINAL, DIA)
    valor = aluguel.calcula_valor()
    multa = aluguel.valor_nominal * 0.02
    dias_atraso = DIA - 15 
    multa_p_dia = aluguel.valor_nominal * 0.001 * dias_atraso
    valor_multas = aluguel.valor_nominal + multa + multa_p_dia
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_multas, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_multas

def test_dia_maior_que_30_MCSF():
    aluguel = Aluguel(VALOR_NOMINAL, 31)
    valor = aluguel.calcula_valor()    
    sys.stderr.write("Esperado {} recebido {}".format(
        -1, valor['valor_calculado']))
    assert valor['valor_calculado'] == -1
