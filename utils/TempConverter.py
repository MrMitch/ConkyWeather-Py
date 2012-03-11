# -*- coding: utf-8 -*-
__author__ = 'MrMitch'

def celsiusToFahrenheit(temp):
    return 5*(int(temp) - 32)/9

def fahrenheitToCelsius(temp):
    return 9*int(temp)/5 + 32

IMPERIAL_SYSTEM = 'i'

METRIC_SYSTEM = 'm'