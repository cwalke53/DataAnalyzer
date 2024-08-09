name = input("Hello user, whats your name? ")
user_pick = int(input(f"Ok, {name}, enter a number between 1 - 100: "))
if user_pick < 60 and (user_pick % 2) == 1:
    print("Odd and less than 60")
elif user_pick < 25 and user_pick > 2 and (user_pick % 2) == 0:
    print("Even and less than 25")
elif user_pick >= 26 and user_pick <= 60 and (user_pick % 2) == 0:
    print("Even and between 26 and 60 inclusive")
elif user_pick > 60 and (user_pick % 2) == 0:
    print(user_pick)
    print("Even and greater than 60")
elif user_pick > 60 and (user_pick % 2) == 1:
    print(user_pick)
    print("Odd and greater than 60")


