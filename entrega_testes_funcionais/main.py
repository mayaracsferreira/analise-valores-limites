#!/usr/bin/env python
# coding=utf-8
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
Aluguel =  os.path.join(current_dir, 'Aluguel.py')
from Aluguel import Aluguel

DIA = 16

aluguel = Aluguel(500.0, DIA)

print("Mayara Ferreira")
print("Aplicação consome a API Web aluguebug")
valor_calculado = aluguel.calcula_valor()
print(valor_calculado)
