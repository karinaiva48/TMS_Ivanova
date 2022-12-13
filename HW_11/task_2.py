"""
2. Реализуйте класс который представляет собой универсальный интерфейс по представлению температуры в шкалах 
Цельсия/Кельвина/Фаренгейта и поддерживает конвертацию значений температуры между этими шкалами 
(https://www.cuemath.com/temperature-conversion-formulas/)
"""

class TemperatureInterface:
    
    def __init__(self, temp) -> None:
        self.C = temp
        self.K = temp
        self.F = temp

    @staticmethod
    def celcius_to_kelvin(temp: float):
        return round(temp + 273.15, 2)

    @staticmethod
    def celcius_to_fahrenheit(temp: float):
        return round(temp * (9/5) + 32, 2)
    
    @staticmethod
    def kelvin_to_celcius(temp: float):
        return round(temp - 273.15, 2)

    @staticmethod
    def kelvin_to_fahrenheit(temp: float):
        return round((temp - 273.15) * (9/5) + 32, 2)

    @staticmethod
    def fahrenheit_to_celsium(temp: float):
        return round((temp - 32) * (5/9), 2)

    @staticmethod
    def fahrenheit_to_kelvin(temp: float):
        return round((temp - 32) * (5/9) + 273.15, 2)


print(TemperatureInterface.celcius_to_kelvin(25))
print(TemperatureInterface.celcius_to_fahrenheit(25))
print(TemperatureInterface.kelvin_to_celcius(285))
print(TemperatureInterface.kelvin_to_fahrenheit(285))
print(TemperatureInterface.fahrenheit_to_celsium(45))
print(TemperatureInterface.fahrenheit_to_kelvin(45))