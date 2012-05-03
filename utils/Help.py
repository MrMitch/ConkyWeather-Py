# -*- coding: utf-8 -*-
__author__ = 'mickael'

def short(path):
    print 'Usage:'
    print '%s [-h]' % path
    print '%s [--help]' % path
    print '%s [api symbol] [unit-system] [location]' % path
    print '%s [api symbol] [unit-system] [location] [current property]' % path
    print '%s [api symbol] [unit-system] [location] [forecast property] [day]' % path
    print '%s [api symbol] [unit-system] [location] [forecast property] [start day] [end day] [separator]' % path

def long(path):
    print 'Usage:'
    print '\n\nHELP'
    print     '—–——'
    print '%s [-h]' % path
    print '\tShow short help.'
    print '%s [--help]' % path
    print '\tShow verbose help.'

    print '\n\nCURRENT WEATHER'
    print     '—–————–——–————–'
    print '%s [api symbol] [unit-system] [location]' % path
    print '\tPrint a brief description of the current weather in the specified location.'
    print "\t\t[api symbol]: 'g' to use GoogleAPI, 'wuYOUR_API_KEY' to use WeatherUndergroudAPI with your API key"
    print "\t\t[unit-system]: 'm' to use the Metric system (°C), 'i' to use the Imperial system (°F)"
    print "\t\t[location]: Your location. Can be a city name, a zip-code, a city name and a country name..."
    print "\t\t            Quotation marks are required to wrap strings containing several words."

    print '\n%s [api symbol] [unit-system] [location] [current weather property]' % path
    print '\tPrint a specific property of the current weather for the specified location.'
    print "\t\t[current weather property]: 'c' to print current textual condition"
    print "\t\t                            't' to print current temperature"
    print "\t\t                            'h' to print current percentage of humidity"
    print "\t\t                            's' to print current symbolic condition (best if displayed using the ConkyWeather.ttf font)"

    print "\n\nFORECAST"
    print     "—–————–—"
    print '%s [api symbol] [unit-system] [location] [forecast property] [day]' % path
    print '\tPrint a specific forecast property for the specified location and a particular day.'
    print "\t\t[forecast property]: 'c' to print forecast textual condition"
    print "\t\t                     't' to print forecast temperatures (max/min)"
    print "\t\t                     's' to print forecast symbolic condition (best if displayed using the ConkyWeather.ttf font)"
    print "\t\t                     'd' to print forecast day name"
    print '\t\t[day]: the 0-based number of the day, 0 meaning today, 1 meaning tomorrow, 2 meaning in two days, ...'

    print '\n%s [api symbol] [unit-system] [location] [forecast property] [start day] [end day] [separator]' % path
    print "\tPrint a specific forecast property for the specified location for every day between [start day] and [end day]"
    print '\tPrint a specific forecast property for the specified location and a particular day.'
    print "\t\t[forecast property]: 'c' to print forecast textual condition"
    print "\t\t                     't' to print forecast temperatures (max/min)"
    print "\t\t                     's' to print forecast symbolic condition (best if displayed using the ConkyWeather.ttf font)"
    print "\t\t                     'd' to print forecast day name"
    print '\t\t[start day]: the 0-based number of the first day, 0 meaning today, 1 meaning tomorrow, 2 meaning in two days, ...'
    print '\t\t[end day]: the 0-based number of the last day, 1 meaning tomorrow, 2 meaning in two days, ...'