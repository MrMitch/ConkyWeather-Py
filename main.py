#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MrMitch'

from sys import argv

argumentsNumber = len(argv)

# main processing
if argumentsNumber >= 4:

    from utils.TempConverter import IMPERIAL_SYSTEM, METRIC_SYSTEM
    from APIs.Google import GoogleAPI
    from APIs.WeatherUnderground import WeatherUndergroundAPI

    # unit system
    if argv[2] == 'm':
        system = METRIC_SYSTEM
    else:
        system = IMPERIAL_SYSTEM

    # API type
    if argv[1] == 'g':
        api = GoogleAPI(argv[3], system)
    elif argv[:2] == 'wu':
        api = WeatherUndergroundAPI(argv[2:], argv[3], system)
    else:
        raise ValueError('Wrong API type %s' % argv[1])


    # first case: no detail asked, print T° + Text + Humidity
    if argumentsNumber == 4:
        print '%s, %s with %s humidity' % (api.condition(), api.temp(), api.humidity())

    # second case: details on current condition
    elif argumentsNumber == 5:
        if argv[4] == 'c':
            print api.condition()
        elif argv[4] == 't':
            print api.temp().encode('utf-8')
        elif argv[4] == 'h':
            print api.humidity()
        elif argv[4] == 's':
            print api.symbol()
        else:
            raise ValueError('Wrong detail parameter %s (must be either c, t, h or s)' % argv[4])

    # third case: forecast
    elif argumentsNumber >= 6:

        if argv[4] not in ['t', 'c', 's', 'd']:
            raise ValueError('Wrong forecast parameter %s (must be either c, t, s or d)')

        # for one day
        if argumentsNumber == 6:
            if argv[4] == 't':
                print api.forecastTemperatures(int(argv[5]))
            elif argv[4] == 'c':
                print api.forecastText(int(argv[5]))
            elif argv[4] == 's':
                print api.forecastSymbol(int(argv[5]))
            else:
                print api.forecastDay(int(argv[5]))

        # for several days
        elif argumentsNumber >= 7:
            if argv[4] == 't':
                forecast = api.forecastTemperaturesList()
            elif argv[4] == 'c':
                forecast = api.forecastTextsList()
            elif argv[4] == 's':
                forecast = api.forecastSymbolsList()
            else:
                forecast = api.forecastDaysList()

            # from today
            if argumentsNumber == 7:
                start = 0
                end = int(argv[5])
            # from any day
            else:
                start = int(argv[5])
                end = int(argv[6])

            # use the last argument as selector
            print argv[argumentsNumber-1].join(forecast[start:end]).encode('utf-8')

elif argumentsNumber == 2:
    import utils.Help as Help
    if argv[1] == '-h':
        Help.short(argv[0])
    elif argv[1] == '--help':
        Help.long(argv[0])
    else:
        raise ValueError('Wrong argument "%s". Try "-h" for short help or "--help" for verbose help') % argv[1]
else:
    raise ValueError('You must provide at least an API, a unit-system and a geolocation.')
