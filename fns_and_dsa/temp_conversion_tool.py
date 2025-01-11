FAHRENHEIT_TO_CELSIUS_FACTOR= 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR= 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature = float(input('Enter the temperature to convert: '))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').strip().upper()
    
    if unit == 'F':
        celsius = convert_to_celsius(temperature)
        print(f'{temperature} F is {celsius:.4f} C')
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f'{temperature} C is {fahrenheit:.4f} F')
    else:
        print('Invalid unit. Please enter F for Fahrenheit or C for Celsius.')
        return

if __name__ == '__main__':
    main()  # Run the main function