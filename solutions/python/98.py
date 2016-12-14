def weather_info (temp):
    c = convertToCelsius(temp)
    return str(c) + (
        ' is freezing temperature' if c < 0.0 
            else ' is above freezing temperature')
    
def convertToCelsius(fahrenheit):
  return (fahrenheit - 32) * (5 / 9.0)