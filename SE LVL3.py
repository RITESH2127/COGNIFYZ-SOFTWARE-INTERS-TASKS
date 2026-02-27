temperature = float(input("Enter the temperature value: "))

print("Choose conversion direction:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    result = (temperature * 9/5) + 32
    print("Temperature in Fahrenheit is:", result)

elif choice == "2":
    result = (temperature - 32) * 5/9
    print("Temperature in Celsius is:", result)

else:
    print("Invalid choice")
