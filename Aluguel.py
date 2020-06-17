#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json


class Aluguel:
    def __init__(self, valor_nominal, dia):
        self.valor_nominal = valor_nominal
        self.dia = dia
        self.API_URL = "https://aluguebug.herokuapp.com/calc?dados={\"valor_nominal\":" + str(
            valor_nominal) + ",\"dia\":" + str(dia) + "}"

    def calcula_valor(self):
        response = requests.get(self.API_URL)
        obj = json.loads(response.json())
        return obj
