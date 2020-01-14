class Fraccion():

    __numerador = 0
    __denominador = 0

    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador

    def __str__(self):
        return f"{self.__numerador} / { self.__denominador }"

    @property
    def numerador(self):
        return self.__numerador

    @numerador.setter
    def numerador(self, newNum):
        self.__numerador = newNum

    @property
    def denominador(self):
        return self.__denominador

    @denominador.setter
    def denominador(self, newNum):
        if denominador == 0:
            return
        self.__denominador = newNum

    def resultado(self):
        return self.__numerador / self.__denominador

    def MulNum(self, num):
        self.__numerador *= num

    def MulFraccion(self, frac):
        self.__numerador *= frac.numerador
        self.__denominador *= frac.denominador

    def SumarFraccion(self, frac):
        self.__numerador = (self.__numerador * frac.__denominador) + (frac.numerador * self.__denominador)
        self.__denominador *= frac.denominador

    def RestarFraccion(self, frac):
        self.__numerador = (self.__numerador * frac.__denominador) - (frac.numerador * self.__denominador)
        self.__denominador *= frac.denominador

    def __mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def Simplificar(self):

        comun_div = self.__mcd(self.__numerador, self.__denominador)
        (num_red, den_red) = (self.__numerador / comun_div, self.__denominador / comun_div)

        self.__numerador = num_red
        self.__denominador = den_red
