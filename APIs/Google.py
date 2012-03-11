# -*- coding: utf-8 -*-
__author__ = 'MrMitch'

from BaseAPI import BaseAPI
from utils.TempConverter import celsiusToFahrenheit, IMPERIAL_SYSTEM

class GoogleAPI(BaseAPI):

    API_NAME = 'GoogleWeather'

    API_VERSION = '1'

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

    def __init__(self, location, system = 'm'):
        BaseAPI.__init__(self, location, system)

        from urllib2 import urlopen, quote
        # ask Google
        googleSocket = urlopen('http://www.google.com/ig/api?weather=%s&hl=en-gb' % quote(self.location()))
        # Google sends a one-line file that needs to be decoded from CP1252 & re-encoded in proper UTF-8
        rawResponse = googleSocket.readline().decode('CP1252').encode('UTF-8')
        googleSocket.close()

        from xml.dom.minidom import parseString
        response = parseString(rawResponse)

        # we got a correct reply
        if response.hasChildNodes():
            reply = response.firstChild
            # if reply is compatible
            if reply.getAttribute('version') == self.API_VERSION :
                # if there has been no error on Google's side
                weather = reply.firstChild
                if weather.firstChild.tagName != 'problem_cause':
                    self.__currentWeather = weather.getElementsByTagName('current_conditions')[0]
                    self.__forecast = weather.getElementsByTagName('forecast_conditions')
                    self.__fullLocation = weather.firstChild.firstChild.getAttribute('data')

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
                raise Exception('API version %s not supported' % reply.getAttribute('version'))
        else:
            raise Exception('Empty reply')




    # LISTS
    def forecastDaysList(self):
        if not len(self.__daysList):
            for forecast in self.__forecast:
                self.__daysList.append(forecast.firstChild.getAttribute('data'))

        return self.__daysList


    def forecastSymbolsList(self):
        if not len(self.__symbolsList):
            for forecast in self.__forecast:
                textualCondition = forecast.lastChild.getAttribute('data')
                self.__symbolsList.append(self._textualToSymbolCondition(textualCondition))

        return self.__symbolsList


    def forecastTextsList(self):
        if not len(self.__textsList):
            for forecast in self.__forecast:
                self.__textsList.append(forecast.lastChild.getAttribute('data'))

        return self.__textsList


    def forecastTemperaturesList(self):
        if not len(self.__tempsList):
            for forecast in self.__forecast:
                low = forecast.getElementsByTagName('low')[0].getAttribute('data')
                high = forecast.getElementsByTagName('high')[0].getAttribute('data')

                if self.system() == IMPERIAL_SYSTEM:
                    low = celsiusToFahrenheit(low)
                    high = celsiusToFahrenheit(high)

                self.__tempsList.append(str(low) + u'°/' + str(high) + u'°')

        return self.__tempsList




    # ATOMS

    def fullLocation(self):
        return self.__fullLocation

    def temp(self):
        if self.__temp == '':
            if self.system() == IMPERIAL_SYSTEM :
                self.__temp = self.__currentWeather.getElementsByTagName('temp_f')[0].getAttribute('data') + u'°'
            else:
                self.__temp = self.__currentWeather.getElementsByTagName('temp_c')[0].getAttribute('data') + u'°'

        return self.__temp


    def text(self):
        if self.__text == '':
            self.__text = self.__currentWeather.getElementsByTagName('condition')[0].getAttribute('data')
        return self.__text



    def symbol(self):
        if self.__symbol == '':
            self.__symbol = self._textualToSymbolCondition(self.text())

        return self.__symbol


    def humidity(self):
        if self.__humidity == '':
            data = self.__currentWeather.getElementsByTagName('humidity')[0].getAttribute('data')
            self.__humidity = data.split(' ')[1]

        return self.__humidity