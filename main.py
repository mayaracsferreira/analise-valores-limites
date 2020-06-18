#!/usr/bin/env python
# coding=utf-8
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
Aluguel =  os.path.join(current_dir, 'Aluguel.py')
from Aluguel import Aluguel

DIA = 16

aluguel = Aluguel(400.0, DIA)

print("Mayara Ferreira")
print("Aplicação consome a API Web aluguebug")
valor_calculado = aluguel.calcula_valor()
print(valor_calculado)

multa = aluguel.valor_nominal * 0.02
dias_passados = DIA - 15
juros_dia = multa * 0.1 * dias_passados
valor_aluguel = aluguel.valor_nominal + multa + juros_dia

print(dias_passados)
print(multa)
print(juros_dia)


print(valor_aluguel)