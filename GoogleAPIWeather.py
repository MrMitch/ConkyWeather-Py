# -*- coding: utf-8 -*-
__author__ = 'MrMitch'

from urllib2 import urlopen, quote
from xml.dom.minidom import parse

class GoogleAPIWeather:

    API_VERSION = '1'

    METRIC_SYSTEM = 'm'

    IMPERIAL_SYSTEM = 'i'

    MAX_FORECAST_DAYS = 4

    CONDITIONS = {
        'Clear':'a',
        'Dust':'7',
        'Flurries':'8',
        'Fog':'9',
        'Freezing Drizzle':'y',
        'Hail':'w',
        'Haze':'0',
        'Icy':'r',
        'Mist':'9',
        'Overcast':'e',
        'Sleet':'y',
        'Smoke':'7',
        'Windy':'6',
        'Mostly Sunny':'b',
        'Partly Sunny':'b',
        'Sunny':'a',
        'Mostly Cloudy':'d',
        'Partly Cloudy':'c',
        'Cloudy':'c',
        'Chance of Snow':'o',
        'Light Snow':'w',
        'Light snow':'w',
        'Rain and Snow':'x',
        'Snow Showers':'v',
        'Snow':'q',
        'Light Rain':'h',
        'Light rain':'h',
        'Chance of Rain':'g',
        'Rain':'v',
        'Scattered Showers':'s',
        'Showers':'s',
        'Chance of Storm':'s',
        'Chance of TStorm':'k',
        'Scattered Thunderstorms':'k',
        'Thunderstorm':'n',
        'Storm':'v'
    }

    def __init__(self, location):
        self.location = str(location)

        # ask Google
        xml = urlopen('http://www.google.com/ig/api?weather=%s&hl=en-gb' % quote(self.location))
        rawResponse = parse(xml)
        xml.close()

        # we got a reply
        if rawResponse.hasChildNodes():
            reply = rawResponse.firstChild
            # if reply is compatible
            if reply.getAttribute('version') == self.API_VERSION :
                # if there has been no error on Google's side
                weather = reply.firstChild
                if weather.firstChild.tagName != 'problem_cause':
                    self.__currentWeather = weather.getElementsByTagName('current_conditions')[0]
                    self.__forecast = weather.getElementsByTagName('forecast_conditions')

                    self.__tempI = ''
                    self.__tempM = ''
                    self.__textualCondition = ''
                    self.__symbolicCondition = ''
                    self.__humidity = ''
                    self.__daysList = []
                    self.__symbolsList = []
                    self.__tempList = []

                    self.__system = self.METRIC_SYSTEM

                else:
                    raise Exception('Unable to retrieve weather information for location %s' % self.location)
            else:
                raise Exception('API version %s not supported' % reply.getAttribute('version'))
        else:
            raise Exception('Empty reply')


    def __textualToSymbolCondition(self, condition):
        if condition in self.CONDITIONS:
            return self.CONDITIONS[condition]
        else:
            return '-'

    ## SETTER
    def setSystem(self, system = 'm'):
        system = str(system).lower()
        if system == self.METRIC_SYSTEM or system == self.IMPERIAL_SYSTEM:
            self.__system = system
        else:
            raise ValueError('Bad value %s for unit system' % system)

    ## Getters
    def temp(self):
        if self.__system == 'i' :
            if self.__tempI == '':
                self.__tempI = self.__currentWeather.getElementsByTagName('temp_f')[0].getAttribute('data') + u'°'
            return self.__tempI
        else :
            if self.__tempM == '':
                self.__tempM = self.__currentWeather.getElementsByTagName('temp_c')[0].getAttribute('data') + u'°'
            return self.__tempM



    def textualCondition(self):
        if self.__textualCondition == '':
            self.__textualCondition = self.__currentWeather.getElementsByTagName('condition')[0].getAttribute('data')
        return self.__textualCondition



    def symbolicCondition(self):
        if self.__symbolicCondition == '':
            self.__symbolicCondition = self.__textualToSymbolCondition(self.textualCondition())

        return self.__symbolicCondition


    def humidity(self):
        if self.__humidity == '':
            data = self.__currentWeather.getElementsByTagName('humidity')[0].getAttribute('data')
            self.__humidity = data.split(' ')[1]

        return self.__humidity

    def forecastDaysList(self):
        if not len(self.__daysList):
            for forecast in self.__forecast:
                self.__daysList.append(forecast.firstChild.getAttribute('data'))

        return self.__daysList


    def forecastSymbolsList(self):
        if not len(self.__symbolsList):
            for forecast in self.__forecast:
                textualCondition = forecast.lastChild.getAttribute('data')
                self.__symbolsList.append(self.__textualToSymbolCondition(textualCondition))

        return self.__symbolsList


    def forecastTemperaturesList(self, separator = '/'):
        separator = str(separator)
        if not len(self.__tempList):
            for forecast in self.__forecast:
                temperatures = list()
                temperatures.append(forecast.getElementsByTagName('low')[0].getAttribute('data') + u'°')
                temperatures.append(forecast.getElementsByTagName('high')[0].getAttribute('data') + u'°')
                self.__tempList.append(separator.join(temperatures))

        return self.__tempList


    def forecastDay(self, index = 1):
        index = int(index)
        if self.MAX_FORECAST_DAYS > index > 0:
            return self.forecastDaysList()[index]
        else:
            raise IndexError('Google API version %s only provides forecast for %i days including today.' % (self.API_VERSION, self.MAX_FORECAST_DAYS))


    def forecastTemperatures(self, index = 1):
        index = int(index)
        if self.MAX_FORECAST_DAYS > index > 0:
            return self.forecastTemperaturesList()[index]
        else:
            raise IndexError('Google API version %s only provides forecast for %i days including today.' % (self.API_VERSION, self.MAX_FORECAST_DAYS))


    def forecastSymbol(self, index = 1):
        index = int(index)
        if self.MAX_FORECAST_DAYS > index > 0:
            return self.forecastSymbolsList()[index]
        else:
            raise IndexError('Google API version %s only provides forecast for %i days including today.' % (self.API_VERSION, self.MAX_FORECAST_DAYS))
