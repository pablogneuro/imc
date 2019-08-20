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
    r'''calcularIndiceMassaCorporal realiza o cálculo do índice de massa corporal (IMC)
        :param pesoQuilos: peso do indivíduo (kg)
        :param alturaMetros: altura do indivíduo (m)
        :return indiceMassaCorporal: índice de massa corporal (IMC)
    '''
    indiceMassaCorporal = (pesoQuilos / (alturaMetros ** 2)) 
    isMuitoAbaixoPeso(indiceMassaCorporal)
    return indiceMassaCorporal


def isMuitoAbaixoPeso(indiceMassaCorporal):
    r'''isMuitoAbaixoPeso verifica se o indivíduo está muito abaixo do peso ideal
        :param indiceMassaCorporal: indice de massa corporal do indivíduo
        :return isMuitoAbaixoPeso: resultado da verificação (indiceMassaCorporal < 17)
    '''
    isMuitoAbaixoPeso = (indiceMassaCorporal < 17)
    print("\n - Está muito abaixo do peso ideal? ", isMuitoAbaixoPeso)
    return isMuitoAbaixoPeso


# Chamada de Métodos

calcularIndiceMassaCorporal(pesoQuilos, alturaMetros)