# -*- coding: utf-8 -*-
__author__ = 'MrMitch'
from BaseAPI import BaseAPI

class WeatherUndergroundAPI(BaseAPI):

    API_NAME = 'WeatherUnderground'

    API_VERSION = '0.1'

    MAX_FORECAST_DAYS = 4

    CONDITIONS = {
        'clear': 'a',
        'flurries': '8',
        'fog': '9',
        'hazy': '0',
        'mostlycloudy': 'd',
        'mostlysunny': 'b',
        'partlysunny': 'd',
        'sleet': 'y',
        'rain': 'v',
        'snow': 'q',
        'sunny': 'a',
        'tstorms': 'k',
        'unknown': '-',
        'cloudy': 'e',
        'partlycloudy': 'c',
        'chanceflurries': '8',
        'chancerain': 'v',
        'chancesleet': 'y',
        'chancesnow': 'q',
        'chancetstorms': 'k'
    }

    def __init__(self, key, location, system = 'm'):
        BaseAPI.__init__(self, location, system)

        from urllib2 import urlopen, quote
        wu = urlopen('http://api.wunderground.com/api/%s/conditions/forecast/q/%s.json' % (str(key), quote(self.location())))
        rawResponse = wu.read()
        wu.close()

        from json import loads
        response = loads(rawResponse)

        if 'error' not in response:
            if response['response']['version'] == self.API_VERSION:
                self.__currentWeather = response['current_observation']
                self.__forecast = response['forecast']['simpleforecast']['forecastday']
                self.__fullLocation = ''

                self.__temp = ''
                self.__text = ''
                self.__symbol = ''
                self.__humidity = ''
                self.__daysList = []
                self.__symbolsList = []
                self.__tempsList = []
                self.__textsList = []
            else:
                raise Exception('Unable to retrieve weather information for location %s' % self.location())
        else:
            raise Exception('Unable to find weather information for %s.\nWeatherUngerground responded: %s' % (self.location(), response['error']['description']))

    def fullLocation(self):
        if self.__fullLocation == '':
            self.__fullLocation = self.__currentWeather['display_location']['full']
        return self.__fullLocation


    ## Getters
    def temp(self):
        if self.__temp == '':
            from utils.TempConverter import IMPERIAL_SYSTEM
            if self.system() == IMPERIAL_SYSTEM:
                self.__temp = str(self.__currentWeather['temp_f']) + u'°'
            else:
                self.__temp = str(self.__currentWeather['temp_c']) + u'°'

        return self.__temp



    def text(self):
        if self.__text == '':
            self.__text = self.__currentWeather['weather']
        return self.__text



    def symbol(self):
        if self.__symbol == '':
            self.__symbol = self.__currentWeather['icon']

        return self.__symbol


    def humidity(self):
        if self.__humidity == '':
            self.__humidity = self.__currentWeather['relative_humidity']

        return self.__humidity

    def forecastDaysList(self):
        if not len(self.__daysList):
            for forecast in self.__forecast:
                self.__daysList.append(forecast['date']['weekday_short'])

        return self.__daysList


    def forecastTextsList(self):
        if not len(self.__textsList):
            for forecast in self.__forecast:
                self.__textsList.append(forecast['conditions'])
        return self.__textsList


    def forecastSymbolsList(self):
        if not len(self.__symbolsList):
            for forecast in self.__forecast:
                textualCondition = forecast['icon']
                self.__symbolsList.append(self._textualToSymbolCondition(textualCondition))

        return self.__symbolsList


    def forecastTemperaturesList(self):
        if not len(self.__tempsList):
            from utils.TempConverter import IMPERIAL_SYSTEM
            for forecast in self.__forecast:
                if self.system() == IMPERIAL_SYSTEM:
                    low = forecast['low']['fahrenheit']
                    high = forecast['high']['fahrenheit']
                else:
                    low = forecast['low']['celsius']
                    high = forecast['high']['celsius']

                self.__tempsList.append(str(low) + u'°/' + str(high) + u'°')

        return self.__tempsList