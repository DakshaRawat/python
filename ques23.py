print("1. Convert C to F")
print("2. Convert F to C")
    
choice = input("Choose the conversion(1 or 2): ")
    
if choice == '1':
    celsius = float(input("Enter "))
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit,"°F")
    
elif choice == '2':
    fahrenheit = float(input("Enter"))
    celsius = (fahrenheit - 32) * 5/9
    print(celsius,"°C")