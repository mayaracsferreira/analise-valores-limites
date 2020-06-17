#!/usr/bin/env python
# coding=utf-8
from Aluguel import Aluguel

aluguel = Aluguel(400.0, 32)

print("Mayara Ferreira")
print("Aplicação consome a API Web aluguebug")
valor_calculado = aluguel.calcula_valor()
print(valor_calculado)
