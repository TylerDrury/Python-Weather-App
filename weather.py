import pyowm

city = "sarnia,Canada"
key ="7085c574f027630c5380ded4133aaf29"

def getWeatherFor(place):
    """Creates a function the will get weather for the given city"""
    degreechar = u'\u00b0' #creates the degree character using unicode
    owm = pyowm.OWM(key) #connects to the api based on the users api key
    observation = owm.weather_at_place(place) #calls the api to retrieve all of the weather data nfrom the given location
    w = observation.get_weather() #gets the weather from the given locationr

    temp = w.get_temperature('celsius') #gets the temperature
    print("\nTemperature for %s: %3.2f%sC" % (place, temp["temp"], degreechar)) #displays the weather data and formated

    wind = w.get_wind() #gives the variable wind the windspeed of the selected area
    print (wind) #diplays the wind data to the user (gusting,speed,direction in degrees

    return w #returns the weather data

if __name__ == "__main__":
    c = raw_input("Enter the city:") #asks the user for a city
    getWeatherFor(c) #calls the getWeatherFor function. can use a hard coded city insted of c

