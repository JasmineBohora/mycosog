import time
def typewriter_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()
print("***************************************************************************************************************************")
typewriter_print("***HI WELCOME!THIS IS THE MATHEMATICAL MIND READER***")
typewriter_print("Think of a number between 1 and 100 and I will try to guess it.")
low=1
high=100
attempt=1
#game boundries ig ToT
typewriter_print("Lets get started!!")
typewriter_print("Respond with 'h' if your number is higher than my guess, 'l' if it is lower, and 'c' if I guessed correctly.")
while low<=high:
    guess= int((low+high) / 2)
    typewriter_print("My guess is: " + str(guess))
    response=input("Is your number higher, lower, or did I guess correctly? (h/l/c): ")
    if response=='h':
        low=guess+1
    elif response=='l':
        high=guess-1
    elif response=='c':
        typewriter_print("Gotcha!Haris bhai,I guessed your number in" + str(attempt) + "attempts!")
        break
    attempt+=1
    if attempt>7:# cus I said 7 is max
        typewriter_print("Abui yesto ta na huna parni")


typewriter_print("If I couldn't guess your number, please make sure you are responding correctly cus hell nah.")
typewriter_print("Thanks for playing! I hope you enjoyed the game.")
print("***************************************************************************************************************************")