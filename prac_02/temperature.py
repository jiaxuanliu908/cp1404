def main():
    celsius_temp = 33
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")

    fahrenheit_temp = 67
    celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp}°F is equal to {celsius_temp}°C")


def celsius_to_fahrenheit(celsius_temp):
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    return fahrenheit_temp


def fahrenheit_to_celsius(fahrenheit_temp):
    celsius_temp = (fahrenheit_temp - 32) * 5 / 9
    return celsius_temp


main()