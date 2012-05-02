#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MrMitch'

from utils.TempConverter import IMPERIAL_SYSTEM, METRIC_SYSTEM
from APIs.Google import GoogleAPI
from APIs.WeatherUnderground import WeatherUndergroundAPI
from sys import argv, stdout

# help function
def displayHelp():
    print 'Usage: ./main.py [-h/--help] [location] [unit-system]'
    print '\t-h/--help\t Display this message and stop the program'
    print '\tlocation\t The name of the location where you\' like to know what\'s the weather like'
    print '\tunit-system\t "m" for Metric unit system, "i" for Imperial unit system'
    exit()

#print argv

# main processing
if len(argv) >= 4:

    if argv[1] == '-h' or argv[1] == '--help':
        displayHelp()
    else:
        # unit system
        if argv[2] == 'm':
            system = METRIC_SYSTEM
        else:
            system = IMPERIAL_SYSTEM

        # API type
        if argv[1] == 'g':
            api = GoogleAPI(argv[3], system)
        elif argv[1] == 'wu':
            api = WeatherUndergroundAPI(argv[3], system)
        else:
            raise ValueError('Wrong API type %s' % argv[1])


        # no detail asked, print T° + Text + Humidity
        if len(argv) == 4:
            print '%s, %s with %s humidity' % (api.text(), api.temp(), api.humidity())
        # details on current condition
        elif len(argv) == 5:
            if argv[4] == 'c':
                print api.text()
            elif argv[4] == 't':
                print api.temp()
            elif argv[4] == 'h':
                print api.humidity()
            elif argv[4] == 's':
                print api.symbol()
            else:
                raise ValueError('Wrong detail parameter %s (must be either c, t, h or s)' % argv[4])
        # forecast
        #elif len(argv) >= 6 & (argv[4][2:].join('') == 'fc'):








else:
    raise ValueError('You must select at least an API, a unit-system and a geolocation.')
