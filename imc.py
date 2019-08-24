# -*- coding: utf-8 -*-

"""
Esse módulo implementa a tarefa 001 ('indice de massa corporal (IMC) da disciplina Fundamentos de Programação e 
Engenharia de Software - PES-001(2019.2) do Programa de Pós-Graduação em Neuroengenharia do Instituto Internacional 
de Neurociências Edmond e Lily Safra (IIN-ELS).

Requisitos e orientações para resolução dessa tarefa encontram-se na wiki do projeto: 
_Wiki: https://github.com/alexaquino/IINELS-PES-001/wiki.

:Authors: Alex Aquino, Bruno Spinelli, Pablo Queiroz, Rodrigo Henrique
:Version: 1.0.0
:License: MIT
"""


# Variáveis Globais 
pesoQuilos = 70.00
alturaMetros = 1.80


# Métodos 

def calcularIndiceMassaCorporal(pesoQuilos, alturaMetros):
    """calcularIndiceMassaCorporal realiza o cálculo do índice de massa corporal (IMC)
        :param pesoQuilos: peso do indivíduo em quilos
        :type pesoQuilos: float
        :param alturaMetros: altura do indivíduo metros
        :type alturaMetros: float
        :return indiceMassaCorporal: índice de massa corporal (IMC)
        :rtype: float
    """
    indiceMassaCorporal = (pesoQuilos / (alturaMetros ** 2)) 
    isMuitoAbaixoPeso(indiceMassaCorporal)
    isAbaixoPeso(indiceMassaCorporal)
    isPesoNormal(indiceMassaCorporal)
    isAcimaPeso(indiceMassaCorporal)
    isMuitoAcimaPeso(indiceMassaCorporal)
    return indiceMassaCorporal


def isMuitoAbaixoPeso(indiceMassaCorporal):
    """isMuitoAbaixoPeso verifica se o indivíduo está muito abaixo do peso ideal
        :param indiceMassaCorporal: indice de massa corporal do indivíduo
        :type indiceMassaCorporal: float
        :return isMuitoAbaixoPeso: resultado da verificação (indiceMassaCorporal < 17)
        :rtype: bool
    """
    isMuitoAbaixoPeso = (indiceMassaCorporal < 17)
    print("\n - Está muito abaixo do peso ideal? ", isMuitoAbaixoPeso)
    return isMuitoAbaixoPeso


def isAbaixoPeso(indiceMassaCorporal):
    """isAbaixoPeso verifica se o indivíduo está abaixo do peso ideal
        :param indiceMassaCorporal: indice de massa corporal do indivíduo
        :type indiceMassaCorporal: float
        :return isAbaixoPeso: resultado da verificação (indiceMassaCorporal >= 17 and indiceMassaCorporal <= 18.5)
        :rtype: bool
    """
    isAbaixoPeso = (indiceMassaCorporal >= 17 and indiceMassaCorporal <= 18.5)
    print("\n - Está abaixo do peso ideal? ", isAbaixoPeso)
    return isAbaixoPeso


def isPesoNormal(indiceMassaCorporal):
    """isPesoNormal verifica se o indivíduo está com o peso ideal
        :param indiceMassaCorporal: indice de massa corporal do indivíduo
        :type indiceMassaCorporal: float
        :return isPesoNormal: resultado da verificação (indiceMassaCorporal >= 18.5 and indiceMassaCorporal indiceMassaCorporal <= 25)
        :rtype: bool
    """
    isPesoNormal = (indiceMassaCorporal >= 18.5 and indiceMassaCorporal <= 25)
    print("\n - Está com o peso ideal? ", isPesoNormal)
    return isPesoNormal
  
  
def isAcimaPeso(indiceMassaCorporal):
    """isAcimaPeso verifica se o indivíduo está acima do peso ideal
        :param indiceMassaCorporal: indice de massa corporal do indivíduo
        :type indiceMassaCorporal: float
        :return isAcimaPeso: resultado da verificação (indiceMassaCorporal >= 25 and indiceMassaCorporal indiceMassaCorporal <= 30)
        :rtype: bool
    """
    isAcimaPeso = (indiceMassaCorporal >= 25 and indiceMassaCorporal <= 30)
    print("\n - Está acima do peso ideal? ", isAcimaPeso)
    return isAcimaPeso


def isMuitoAcimaPeso(indiceMassaCorporal):
    """isMuitoAcimaPeso verifica se o indivíduo está muito acima do peso ideal
        :param indiceMassaCorporal: indice de massa corporal do indivíduo
        :type indiceMassaCorporal: float
        :return isMuitoAcimaPeso: resultado da verificação (indiceMassaCorporal > 30)
        :rtype: bool
    """
    isMuitoAcimaPeso = (indiceMassaCorporal > 30)
    print("\n - Está muito acima do peso ideal? ", isMuitoAcimaPeso)
    return isMuitoAcimaPeso


# Chamada de Métodos
calcularIndiceMassaCorporal(pesoQuilos, alturaMetros)
