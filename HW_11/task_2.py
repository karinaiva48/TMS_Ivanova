class TemperatureInterface:

    def __init__(self, temp) -> None:
        self.C = temp
        self.K = temp + 273
        self.F = ...

    @staticmethod
    def celcius_to_kelvin(temp: float):
        return temp + 273.15
    
    @staticmethod
    def kelvin_to_celcius(temp: float):
        return temp - 273.15
current_temp = input()
current_temp = float(current_temp)
x = TemperatureInterface.kelvin_to_celcius(current_temp)
print(x)
