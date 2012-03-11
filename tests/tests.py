#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MrMitch'

from sys import argv
from APIs import Google, WeatherUnderground

print "Arguments:\n%s" % str(argv)

def runTest(weather):
    print '\n\n-->Testing %s' % weather.API_NAME
    print '\n## Current weather in %s ##' % weather.location()
    print 'Temp: %s' % weather.temp()
    print 'Humidity: %s' % weather.humidity()
    print 'Condition (full): %s' % weather.text()
    print 'Condition (symbolic): %s' % weather.symbol()
    print '\n## Forecast for %s ##' % weather.location()
    print '     '.join(weather.forecastDaysList())
    print ' '.join(weather.forecastTemperaturesList())
    print ' ' + '       '.join(weather.forecastSymbolsList())

    future = 2

    print '\nin %i days we are: %s' % (future, weather.forecastDay(future))
    print 'forecast temps are: %s' % weather.forecastTemperatures(future)
    print 'forecast condition is: %s' % weather.forecastText(future)
    print 'forecast symbol is: %s' % weather.forecastSymbol(future)

location = 'Strasbourg'

runTest(Google.GoogleAPI(location))

print

runTest(WeatherUnderground.WeatherUndergroundAPI('12e96659693addd5', location))
