from abc import ABC, abstractmethod


class ConversionMonedas(ABC):
    """
      Declaramos la clase lase abstracta llamada ConversionMonedas
      """

    @abstractmethod
    def conversion(self, total_ingresado, moneda_inicio, moneda_final):
        """Declaramos un metodo abstracto llamada conversion
        :arg
        total_ingresado: Total ingresado
        moneda_inicio: Moneda Origen
        moneda_final: Moneda Destino
           """
        pass


class ConversionUSD(ConversionMonedas):
    """Implemetamos la conversion de USD para otras divisas
    :arg
        total_ingresado: Total ingresado
        moneda_inicio: Moneda Origen
        moneda_final: Moneda Destino
    """

    def conversion(self, total_ingresado, moneda_inicio, moneda_final):
        total_ingresado = float(total_ingresado)
        if moneda_inicio == "USD" and moneda_final == "EUR":
            return total_ingresado * 0.92
        elif moneda_inicio == "USD" and moneda_final == "PMX":
            return total_ingresado * 18.76
        elif moneda_inicio == "USD" and moneda_final == "PARG":
            return total_ingresado * 932.27
        elif moneda_inicio == "USD" and moneda_final == "CHF":
            return total_ingresado * 1.8
        elif moneda_inicio == "USD" and moneda_final == "AUD":
            return total_ingresado * 1.2
        elif moneda_inicio == "USD" and moneda_final == "CAD":
            return total_ingresado * 1.4
        else:
            raise ValueError('La moneda ingresada es la misma en ambos campos')


class ConversionEUR(ConversionMonedas):
    """Implemetamos la conversion de EUR para otras divisas

    :arg
        total_ingresado: Total ingresado
        moneda_inicio: Moneda Origen
        moneda_final: Moneda Destino
    """

    def conversion(self, total_ingresado, moneda_inicio, moneda_final):
        total_ingresado = float(total_ingresado)
        if moneda_inicio == "EUR" and moneda_final == "USD":
            return total_ingresado * 1.08
        elif moneda_inicio == "EUR" and moneda_final == "PMX":
            return total_ingresado * 20.3
        elif moneda_inicio == "EUR" and moneda_final == "PARG":
            return total_ingresado * 1008.29
        elif moneda_inicio == "EUR" and moneda_final == "CHF":
            return total_ingresado * 0.96
        elif moneda_inicio == "EUR" and moneda_final == "AUD":
            return total_ingresado * 1.65
        elif moneda_inicio == "EUR" and moneda_final == "CAD":
            return total_ingresado * 1.5
        else:
            raise ValueError('La moneda ingresada es la misma en ambos campos')


class ConversionCHF(ConversionMonedas):
    """Implemetamos la conversion de CHF para otras divisas
    :arg
        total_ingresado: Total ingresado
        moneda_inicio: Moneda Origen
        moneda_final: Moneda Destino
    """

    def conversion(self, total_ingresado, moneda_inicio, moneda_final):
        total_ingresado = float(total_ingresado)
        if moneda_inicio == "CHF" and moneda_final == "USD":
            return total_ingresado * 1.13
        elif moneda_inicio == "CHF" and moneda_final == "PMX":
            return total_ingresado * 21.26
        elif moneda_inicio == "CHF" and moneda_final == "PARG":
            return total_ingresado * 1055.48
        elif moneda_inicio == "CHF" and moneda_final == "EUR":
            return total_ingresado * 1.05
        elif moneda_inicio == "CHF" and moneda_final == "AUD":
            return total_ingresado * 1.73
        elif moneda_inicio == "CHF" and moneda_final == "CAD":
            return total_ingresado * 1.57
        else:
            raise ValueError('La moneda ingresada es la misma en ambos campos')


class ConversionAUD(ConversionMonedas):
    """Implemetamos la conversion de AUD para otras divisas
    :arg
        total_ingresado: Total ingresado
        moneda_inicio: Moneda Origen
        moneda_final: Moneda Destino
    """

    def conversion(self, total_ingresado, moneda_inicio, moneda_final):
        total_ingresado = float(total_ingresado)
        if moneda_inicio == "AUD" and moneda_final == "USD":
            return total_ingresado * 0.65
        elif moneda_inicio == "AUD" and moneda_final == "PMX":
            return total_ingresado * 12.27
        elif moneda_inicio == "AUD" and moneda_final == "PARG":
            return total_ingresado * 609.73
        elif moneda_inicio == "AUD" and moneda_final == "EUR":
            return total_ingresado * 0.6
        elif moneda_inicio == "AUD" and moneda_final == "CHF":
            return total_ingresado * 0.58
        elif moneda_inicio == "AUD" and moneda_final == "CAD":
            return total_ingresado * 0.91
        else:
            raise ValueError('La moneda ingresada es la misma en ambos campos')


class ConversionCAD(ConversionMonedas):
    """Implemetamos la conversion de CAD para otras divisas
    :arg
        total_ingresado: Total ingresado
        moneda_inicio: Moneda Origen
        moneda_final: Moneda Destino
    """

    def conversion(self, total_ingresado, moneda_inicio, moneda_final):
        total_ingresado = float(total_ingresado)
        if moneda_inicio == "CAD" and moneda_final == "USD":
            return total_ingresado * 0.72
        elif moneda_inicio == "CAD" and moneda_final == "PMX":
            return total_ingresado * 13.54
        elif moneda_inicio == "CAD" and moneda_final == "PARG":
            return total_ingresado * 673.1
        elif moneda_inicio == "CAD" and moneda_final == "EUR":
            return total_ingresado * 0.67
        elif moneda_inicio == "CAD" and moneda_final == "CHF":
            return total_ingresado * 0.64
        elif moneda_inicio == "CAD" and moneda_final == "AUD":
            return total_ingresado * 1.10
        else:
            raise ValueError('La moneda ingresada es la misma en ambos campos')


class ConversionMetodoFactory:
    """"Se implementa un patron de diseño Factory Method
    Segun la moneda ingresada se devolvera una clase de conversion
    """

    @staticmethod
    def getConversion(moneda_ingresada):
        if moneda_ingresada == 'USD':
            return ConversionUSD()
        elif moneda_ingresada == 'AUD':
            return ConversionAUD()
        elif moneda_ingresada == 'CHF':
            return ConversionCHF()
        elif moneda_ingresada == 'CAD':
            return ConversionCAD()
        elif moneda_ingresada == 'EUR':
            return ConversionEUR()
        else:
            raise ValueError('La moneda ingresada es incorrecta')
