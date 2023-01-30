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
