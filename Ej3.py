class Fecha():

    code = ""

    def __init__(self, fStr):
        self.code = fStr

    def fechaCorrecta(self) -> bool:
        if len(self.code) != 8:
            return False

        if not self.code.isdigit():
            return False

        if self.dia > self.maxDiasMes:
            return False

        if self.mes > 12:
            return False

        if not self.esBisiesto and self.mes == 2 and self.dia > 8:
            return False

        return True

    def fechaMas1Dia(self) -> str:
        self.dia += 1

        if self.dia > self.maxDiasMes:
            self.dia = 1
            self.mes += 1

        if self.mes > 12:
            self.mes = 1
            self.anyo += 1

        self = Fecha(self.dia, self.mes, self.anyo)

    def fechaMasNDias(self, dias: int) -> str:
        for i in range(dias):
            self.code = self.fechaMas1Dia()

        return self.code

    def fechaMenos1Dia(self) -> str:

        self.dia -= 1

        if self.dia < 1:
            self.mes -= 1
            newMes = Fecha.fecha(self.dia, self.mes, self.anyo)
            self.dia = newMes.maxDiasMes

        if self.mes < 1:
            self.mes = 12
            self.anyo -= 1

        return fecha(self.dia, self.mes, self.anyo)

    def fechaMenosNDias(self, dias: int) -> str:
        for i in range(dias):
            fecha = self.fechaMenos1Dia()

        return fecha

    @property
    def esBisiesto(self) -> bool:
        return (self.anyo % 4 == 0 and self.anyo % 100 != 0) or (self.anyo % 400 == 0)

    def comparaFechas(self, fecha2) -> int:
        year2 = fecha2.anyo
        month2 = fecha2.mes
        day2 = fecha2.dia

        if self.anyo < year2:
            return -1
        elif year2 < self.anyo:
            return 1
        else:
            if self.mes < month2:
                return -1
            elif month2 < self.mes:
                return 1
            else:
                if self.dia < day2:
                    return -1
                elif day2 < self.dia:
                    return 1
                else:
                    return 0

    def fechaFormateada(self) -> str:
        day = self.dia
        month = self.nombreMes
        year = self.anyo

        return f"{day} de {month} de {year}"

    @property
    def anyo(self) -> int:
        return int(self.code[0:4])

    MESES = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre"
    ]

    @property
    def mes(self) -> int:
        return int(self.code[4:6])

    @property
    def nombreMes(self) -> int:
        return self.MESES[self.mes - 1]

    @property
    def dia(self) -> int:
        return int(self.code[6:8])

    @staticmethod
    def fecha(d, m, a: int):
        day = str(d)
        month = str(m)
        year = str(a)

        if len(day) < 2:
            day = "0"+day

        if len(month) < 2:
            month = "0" + month

        if len(year) < 4:
            year = "0"*(4-len(year)) + year

        return Fecha(f"{year}{month}{day}")

    @property
    def maxDiasMes(self) -> int:

        if (not self.esBisiesto and self.mes == 2):
            return 28
        elif self.mes == 2:
            return 29

        if ((self.mes < 8 and (self.mes % 2 == 0)) or (self.mes >= 8 and self.mes % 2 != 0)):
            return 30
        else:
            return 31
