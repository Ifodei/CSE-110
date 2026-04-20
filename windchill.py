#defining the program
def wind_chill(temp_fahrenheit, wind_speed):
    wind_chill_temp = 35.74 +(0.6215 * temp_fahrenheit) -(35.75 *(wind_speed ** 0.16)) + (0.4275 * temp_fahrenheit * (wind_speed ** 0.16))
    return wind_chill_temp

def celsius_to_fahrenheit(temp_celsius):
    #celsius to fahrenheit conversion formula
    temp_fahrenheit = (temp_celsius * 9/5) +32
    return temp_fahrenheit

temp_input = float(input("What is the temperature?"))
scale = input("Fahrenheit or Celsius (F/C)?").upper()
if scale == "C" :
    temp_fahrenheit = celsius_to_fahrenheit(temp_input)
elif scale == "F" :
    temp_fahrenheit = temp_input
else :
    print("Invalid input, Please enter either 'F' or 'C'.")

for wind_speed in range(5, 61, 5):
    windchill = wind_chill(temp_fahrenheit, wind_speed)
    #format windchill to 2dp
    windchill_formatted = f"{windchill:.2f}"
    print(f"At temperature {temp_input}°{scale}, and windspeed {wind_speed} mph, the windchill is : {windchill_formatted}")