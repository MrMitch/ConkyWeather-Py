#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MrMitch'

from utils.TempConverter import IMPERIAL_SYSTEM, METRIC_SYSTEM
from APIs.Google import GoogleAPI
from sys import argv, stdout

location = 'New York'
system = METRIC_SYSTEM


def displayHelp():
    print 'Usage: ./main.py [-h/--help] [location] [unit-system]'
    print '\t-h/--help\t Display this message and stop the program'
    print '\tlocation\t The name of the location where you\' like to know what\'s the weather like'
    print '\tunit-system\t "m" for Metric unit system, "i" for Imperial unit system'
    exit()


try:
    if len(argv) >= 2:

        if argv[1] == '-h' or argv[1] == '--help':
            displayHelp()
        else:
            location = argv[1]

        if len(argv) >= 3:
            system = argv[2]
        else:
            print 'No unit system specified.'
    else:
        print 'No location specified.'

    stdout.write('Fetching weather for %s ' % location)

    if system == IMPERIAL_SYSTEM:
        print 'using imperial unit system'
    else:
        print 'using metric unit system'

    weather = GoogleAPI(location, system)

    print '\n## Current weather in %s ##' % weather.fullLocation()
    print 'Temp: %s' % weather.temp()
    print 'Humidity: %s' % weather.humidity()
    print 'Condition (full): %s' % weather.text()
    print 'Condition (symbolic): %s' % weather.symbol()
    print '\n## Forecast for %s ##' % location
    print '     '.join(weather.forecastDaysList())
    print ' '.join(weather.forecastTemperaturesList())
    print ' ' + '       '.join(weather.forecastSymbolsList())

    future = 2
    
    print '\nin %i days we are: ' % future + weather.forecastDay(future)
    print 'forecast temps are: ' + weather.forecastTemperatures(future)
    print 'forecast condition is: ' + weather.forecastText(future)
    print 'forecast symbol is: ' + weather.forecastSymbol(future)

except Exception:
    print 'Wrong parameters. Try "./main.py -h" or "./main.py --help" for more information.'