temp= eval(input("Enter temperature in Celsius: "))
ftemp = 9/5*temp*32
print("in fahrenheit that is: ", ftemp)
if ftemp > 212:
    print("The temperature is Above boiling point")
if ftemp < 32:
    print("The tempertaure is Below the freezing point")
