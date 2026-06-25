temp= int(input("Whats the temperature in Celsius? "))
humidity= int(input("Whats the humidity in percentage? "))
if (temp >= 30):
    if (humidity >= 60):
        print("Your area is prone to forest fire ToT.")
    else:
         print("Not much risk of forest fire for now .")
else:
        print("Your area is not prone to forest fire.You safe for now.")