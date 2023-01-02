class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        output=[]
        kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        output.append(kelvin)
        output.append( Fahrenheit)
        return output