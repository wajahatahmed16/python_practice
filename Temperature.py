from os import system
from msvcrt import getch
def t_convert(temp,Cel=1):
    if Cel==1:
        try:
            return (temp * 9/5) + 32
        except:
            return "Error in Data!!!"

    else:
        try:
            return (temp - 32) * 5/9
        except:
            print("Error in Data!!!")

system("cls")

while True:

    print("||==Temperature Convdersion==||")
    print("Press 1: Convert Farenheit to Celcius")
    print("Press 2: Convert Celcius to Farenheit")
    print("Press 3: Exit")

    c=(getch()).decode("utf-8")

    if c=="1":
        system("cls")

        print("||==Farenheit to Celcius==||")
        try:
            t=float(input("Enter Tempreature : "))
            print(f"({t}°F − 32) × 5/9 = {t_convert(t,0)}°C")
        except:
            print("Error in Data!!!")
        print("\nPress Any Key to Continue!!!")
        getch()
        system("cls") 

    elif c=="2":
        system("cls")

        print("||==Celcius to Farenheit==||")
        try:
            t=float(input("Enter Tempreature : "))
            print(f"({t}°C × 9/5) + 32 = = {t_convert(t,1)}°F")
        except:
            print("Error in Data!!!")
        print("\nPress Any Key to Continue!!!")
        getch()    
        system("cls")
    elif c=="3":
        break
    else:
        system("cls")
        print("Unknown Selection!!!")
print("Farewell")