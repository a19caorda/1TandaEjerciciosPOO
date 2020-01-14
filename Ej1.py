import math


class Tiempo():

    __segundos = 0

    def __init__(self, horas, minutos, segundos):
        self.__segundos = segundos + (minutos * 60) + (horas * 3600)

    @property
    def segundos(self):
        return self.__segundos % 60

    @property
    def minutos(self):
        return math.floor(self.__segundos / 60 % 60)

    @property
    def horas(self):
        return math.floor(self.__segundos / 3600)

    def __str__(self):
        return f"{self.horas}h {self.minutos}m {self.segundos}s"

    def SumarTiempo(self, time):
        self.__segundos += time.segundos + (time.minutos * 60) + (time.horas * 3600)
        if self.__segundos < 0:
            self.__segundos = 0

    def RestarTiempo(self, time):
        self.__segundos -= time.segundos + (time.minutos * 60) + (time.horas * 3600)
        if self.__segundos < 0:
            self.__segundos = 0

    def Sumar(self, segundos=0, minutos=0, horas=0):
        self.__segundos += segundos + (minutos * 60) + (horas * 3600)
        if self.__segundos < 0:
            self.__segundos = 0

    def Restar(self, segundos=0, minutos=0, horas=0):
        self.__segundos -= segundos + (minutos * 60) + (horas * 3600)
        if self.__segundos < 0:
            self.__segundos = 0
