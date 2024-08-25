#Temperature Conventer shte priema chislo i shte go preobrazuva ot C* v F i obratno
# shte ima funkci za suotvetnoto preobrazuvane



def conv_from_Celcium_to_Fahrenheit (farenheit):
    farenheit *= 1.8
    farenheit += 32
    return farenheit

def conv_from_Fahrenheit_to_Celcium(celcium):

    celcium = celcium - 32
    celcium = celcium / 1.8
    return celcium

#array s opciite
options = ("Celcium", "Fahrenheit")
#Introduction
print("Welcome to the temperature conventer")
# The 2 variables
number = float(input("How many degrees?: "))
measurement = input("Celcium or Fahrenheit? : ")


while measurement not in options:
    measurement = input("Celcium or Fahrenheit? : ")

if measurement == "Celcium":
    print(f"{number}°C is equal to {conv_from_Celcium_to_Fahrenheit(number )} °F ")
    print("Formula: F = ( C * 1.8) + 32 ")

else:
    print(f"{number} °F is equal to {conv_from_Fahrenheit_to_Celcium(number)}°C ")
    print("Formula: C = ( F - 32 ) / 1.8 ")
print("Thank you for using Temperature Conventer")


