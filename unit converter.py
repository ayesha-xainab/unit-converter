def length_converter(value, from_unit, to_unit):
    #conversion to meters
    length_conversion_factors = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34,
        'feet': 0.3048
    }
    
    if from_unit not in length_conversion_factors or to_unit not in length_conversion_factors:
        return "Invalid length units"
    
    #convert values to meters, then the asked unit
    value_in_meters = value * length_conversion_factors[from_unit]
    converted_value = value_in_meters / length_conversion_factors[to_unit]
    
    return round(converted_value, 3)

def weight_converter(value, from_unit, to_unit):
    #conversion to kilograms
    weight_conversion_factors = {
        'kilograms': 1,
        'grams': 0.001,
        'pounds': 0.453592,
        'ounces': 0.0283495
    }
    
    if from_unit not in weight_conversion_factors or to_unit not in weight_conversion_factors:
        return "Invalid weight units"
    
    #convert values to kilograms, then the asked unit
    value_in_kilograms = value * weight_conversion_factors[from_unit]
    converted_value = value_in_kilograms / weight_conversion_factors[to_unit]
    
    return round(converted_value, 2)

#Temperature Conversion
def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return round((value * 9/5) + 32, 2)
        elif to_unit == 'kelvin':
            return round(value + 273.15, 2)
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return round((value - 32) * 5/9, 2)
        elif to_unit == 'kelvin':
            return round((value - 32) * 5/9 + 273.15, 2)
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return round(value - 273.15, 2)
        elif to_unit == 'fahrenheit':
            return round((value - 273.15) * 9/5 + 32, 2)
    
    return "Invalid temperature units"

#Angle Conversion
def angle_converter(value, from_unit, to_unit):
    #conversion to degrees
    angle_conversion_factors = {
        'degrees': 1,
        'radians': 57.2958
    }
    
    if from_unit not in angle_conversion_factors or to_unit not in angle_conversion_factors:
        return "Invalid angle units"
    
    #convert values to degrees, then to the asked unit
    value_in_degrees = value * angle_conversion_factors[from_unit]
    converted_value = value_in_degrees / angle_conversion_factors[to_unit]
    
    return round(converted_value, 1)

def time_converter(value, from_unit, to_unit):
    #Conversion to seconds
    time_conversion_factors = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    
    if from_unit not in time_conversion_factors or to_unit not in time_conversion_factors:
        return "Invalid time units"
    
    #convert values to seconds, then the asked unit
    value_in_seconds = value * time_conversion_factors[from_unit]
    converted_value = value_in_seconds / time_conversion_factors[to_unit]
    
    return converted_value

def main():
    #Main Loop
    while True:
        print(" Unit Converter")
        print("\n1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Angles")
        print("5. Time")
        print("6. Exit")
        
        choice = input("\nChoose your option: ") #Getting user's choice

        #Length Conversion
        if choice == '1':
            value = float(input("\nEnter the value to convert: "))
            print("\nUnits = meters, kilometers, miles, feet")
            from_unit = input("Enter the unit to convert from: ").lower()
            to_unit = input("Enter the unit to convert to: ").lower()
            result = length_converter(value, from_unit, to_unit)
            print(f"\n{value} {from_unit} is equal to {result} {to_unit}")
        #Weight Conversion
        elif choice == '2':
            value = float(input("\nEnter the value to convert: "))
            print("\nUnits = kilograms, grams, pounds, ounces")
            from_unit = input("Enter the unit to convert from: ").lower()
            to_unit = input("Enter the unit to convert to: ").lower()
            result = weight_converter(value, from_unit, to_unit)
            print(f"\n{value} {from_unit} is equal to {result} {to_unit}")
        #Temperature Conversion
        elif choice == '3':
            value = float(input("\nEnter the value to convert: "))
            print("\nUnits = celsius, fahrenheit, kelvin")
            from_unit = input("Enter the unit to convert from: ").lower()
            to_unit = input("Enter the unit to convert to: ").lower()
            result = temperature_converter(value, from_unit, to_unit)
            print(f"\n{value} {from_unit} is equal to {result} {to_unit}")
        #Angle Conversion
        elif choice == '4':
            value = float(input("\nEnter the value to convert: "))
            print("\nUnits = degrees, radians")
            from_unit = input("Enter the unit to convert from: ").lower()
            to_unit = input("Enter the unit to convert to: ").lower()
            result = angle_converter(value, from_unit, to_unit)
            print(f"\n{value} {from_unit} is equal to {result} {to_unit}")
        #Time Conversion
        elif choice == '5':
            value = float(input("\nEnter the value to convert: "))
            print("\nUnits = seconds, minutes, hours, days")
            from_unit = input("Enter the unit to convert from: ").lower()
            to_unit = input("Enter the unit to convert to: ").lower()
            result = time_converter(value, from_unit, to_unit)
            print(f"\n{value} {from_unit} is equal to {result} {to_unit}")
        #Exit 
        elif choice == '6':
            break
        #Invalid input
        else:
            print("Invalid choice. Please try again.")
        print("\n")

if __name__ == "__main__":
    main()
