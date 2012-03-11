#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MrMitch'

from sys import argv
from APIs import Google, WeatherUnderground

print "%s\n" % str(argv)

#a = WeatherUnderground.WeatherUndergroundAPI('12e96659693addd5', 'Strasbourg, France')
weather = Google.GoogleAPI('strasbourg')
weather = WeatherUnderground.WeatherUndergroundAPI('12e96659693addd5', 'Strasbourg, France')

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

print '\nin %i days we are: ' % future + weather.forecastDay(future)
print 'forecast temps are: ' + weather.forecastTemperatures(future)
print 'forecast condition is: ' + weather.forecastText(future)
print 'forecast symbol is: ' + weather.forecastSymbol(future)