# -*- coding: utf-8 -*-
__author__ = 'MrMitch'

class BaseAPI:

    API_NAME = ''

    API_VERSION = ''

    MAX_FORECAST_DAYS = 0

    CONDITIONS = {}

    def __init__(self, location, system):
        self.__location = str(location)
        self.__setSystem(system)

    def __setSystem(self, system):
        system = str(system).lower()
        from utils.TempConverter import IMPERIAL_SYSTEM, METRIC_SYSTEM

        if system == METRIC_SYSTEM or system == IMPERIAL_SYSTEM:
            self.__system = system
        else:
            raise ValueError('Bad value %s for unit system.' % system)



    def _textualToSymbolCondition(self, condition):
        if condition in self.CONDITIONS:
            return self.CONDITIONS[condition]
        else:
            return '-'



    ## default getters
    def system(self):
        return self.__system


    def location(self):
        return self.__location




    # LISTS
    def forecastDaysList(self):
        pass

    def forecastSymbolsList(self):
        pass

    def forecastTextsList(self):
        pass

    def forecastTemperaturesList(self):
        pass



    # ATOMS
    def fullLocation(self):
        pass

    def temp(self):
        pass

    def text(self):
        pass

    def symbol(self):
        pass

    def humidity(self):
        pass


    # should not be re-implemented
    def forecastDay(self, index = 1):
        index = int(index)
        if abs(index) < self.MAX_FORECAST_DAYS:
            return self.forecastDaysList()[index]
        else:
            raise IndexError('%s v%s only provides forecast for %i days including today.' % (self.API_NAME, self.API_VERSION, self.MAX_FORECAST_DAYS))

    def forecastTemperatures(self, index = 1):
        index = int(index)
        if abs(index) < self.MAX_FORECAST_DAYS:
            return self.forecastTemperaturesList()[index]
        else:
            raise IndexError('%s v%s only provides forecast for %i days including today.' % (self.API_NAME, self.API_VERSION, self.MAX_FORECAST_DAYS))

    def forecastSymbol(self, index = 1):
        index = int(index)
        if abs(index) < self.MAX_FORECAST_DAYS:
            return self.forecastSymbolsList()[index]
        else:
            raise IndexError('%s v%s only provides forecast for %i days including today.' % (self.API_NAME, self.API_VERSION, self.MAX_FORECAST_DAYS))

    def forecastText(self, index = 1):
        if abs(index) < self.MAX_FORECAST_DAYS:
            return self.forecastTextsList()[index]
        else:
            raise IndexError('%s v%s only provides forecast for %i days including today.' % (self.API_NAME, self.API_VERSION, self.MAX_FORECAST_DAYS))
