# -*- coding: utf-8 -*-

'''
Esse arquivo implementa a tarefa 001 ('indice de massa corporal (IMC) da disciplina "Fundamentos de Programação e 
Engenharia de Software - PES-001(2019.2)" do Programa de Pós-Graduação em Neuroengenharia do Instituto Internacional 
de Neurociências Edmond e Lily Safra (IIN-ELS).

Requisitos e orientações para execução dessa tarefa encontram-se na wiki do projeto: 
https://github.com/alexaquino/IINELS-PES-001/wiki.

:author:
    Alex Aquino
    Bruno Spinelli
    Pablo
    Rodrigo

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
    isAbaixoPeso(indiceMassaCorporal)
    return indiceMassaCorporal


def isMuitoAbaixoPeso(indiceMassaCorporal):
    r'''isMuitoAbaixoPeso verifica se o indivíduo está muito abaixo do peso ideal
        :param indiceMassaCorporal: indice de massa corporal do indivíduo
        :return isMuitoAbaixoPeso: resultado da verificação (indiceMassaCorporal < 17)
    '''
    isMuitoAbaixoPeso = (indiceMassaCorporal < 17)
    print("\n - Está muito abaixo do peso ideal? ", isMuitoAbaixoPeso)
    return isMuitoAbaixoPeso


def isAbaixoPeso(indiceMassaCorporal):
    r'''isAbaixoPeso verifica se o indivíduo está abaixo do peso ideal
        :param indiceMassaCorporal: indice de massa corporal do indivíduo
        :return isAbaixoPeso: resultado da verificação (indiceMassaCorporal >= 17 and indiceMassaCorporal <= 18.5)
    '''
    isAbaixoPeso = (indiceMassaCorporal >= 17 and indiceMassaCorporal <= 18.5)
    print("\n - Está abaixo do peso ideal? ", isAbaixoPeso)
    return isAbaixoPeso


# Chamada de Métodos
calcularIndiceMassaCorporal(pesoQuilos, alturaMetros)