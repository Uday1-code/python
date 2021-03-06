import math

class WindChill:

    def findWeatherCondition(self):   # finding weather condition
        """
        calculating weather condition from temp and wind speed
        :return: Weather condition value as per formula
        """
        weather = 35.74+(0.6215*self.temp)+(0.4275*self.temp-35.75)*math.pow(self.windSpeed, 0.16)
        return weather

    def inputTempAndWindSpeed(self):
        """
         taking input from user for temp and wind speed
        :return:
        """
        while True:
            try:
                self.temp = float(input("Enter temperature in fahrenheit should be less than 50: "))
                self.windSpeed = float(input("Enter wind speed between 3 to 120 miles per our: "))
                if self.temp > 50:
                    print("Temperature should be less then 50 fahrenheit")
                    continue
                if 3 > self.windSpeed > 120:
                    print("Wind speed should be between 3 to 120")
                    self.inputTempAndWindSpeed()
                    continue
                break
            except ValueError:
                print("not valid float type")


if __name__ == "__main__":
    windchill = WindChill()
    windchill.inputTempAndWindSpeed()
    weather = windchill.findWeatherCondition()
    print("Weather condition value is: ", weather)
