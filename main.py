#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MrMitch'

from GoogleAPIWeather import GoogleAPIWeather
import sys

if len(sys.argv) >= 2:
    location = sys.argv[1]
else:
    location = 'New York'
    sys.stdout.write('No location specified. ')

print 'Fetching weather for %s' % location

weather = GoogleAPIWeather(location)

print '\n## %s\'s current weather ##' % location
print 'Temp: %s' % weather.temp()
print 'Humidity: %s' % weather.humidity()
print 'Condition (full): %s' % weather.textualCondition()
print 'Condition (symbolic): %s' % weather.symbolicCondition()

print '\n## Forecast for %s ##' % location
print '     '.join(weather.forecastDaysList())
print ' '.join(weather.forecastTemperaturesList())
print ' ' + '       '.join(weather.forecastSymbolsList())
