print("Welcome to the login system.")
password= 1987
while  True:
    trypass = int(input("Enter your password: "))
    if trypass == password:
        print("Login successful!")
        break
    else:
     print("Incorrect password. Please try again.")
     
