# -*- coding: utf-8 -*-

'''
Esse arquivo implementa a tarefa 001 ('indice de massa corporal (IMC) da disciplina "Fundamentos de Programação e 
Engenharia de Software - PES-001(2019.2)" do Programa de Pós-Graduação em Neuroengenharia do  Instituto Internacional 
de Neurociências Edmond e Lily Safra (IIN-ELS).

Requisitos e orientações para execução dessa tarefa encontram-se na wiki do projeto, na seção tarefa 1 - IMC.

:autores:
    - Alex Aquino.
    - Bruno Guedes Spinelli

:version: 1.0.0
:license: MIT
'''

# Variáveis Globais 

pesoQuilos = 70.00
alturaMetros = 1.80


# Métodos 

def calcularIndiceMassaCorporal(pesoQuilos, alturaMetros):
    r'''realiza o cálculo do IMC
        :param pesoQuilos: peso do indivíduo (kg)
        :param alturaMetros: altura do indivíduo (m)
    '''
    indiceMassaCorporal = (pesoQuilos / (alturaMetros ** 2)) 
    return indiceMassaCorporal


# Chamada de Métodos

print("- Índice de Massa Corporea (IMC): ", calcularIndiceMassaCorporal(pesoQuilos, alturaMetros))
