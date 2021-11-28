print("welcome")

secret_number = 42

guess = input("writing your number: ")

guess_int = int(guess)

print("your writed : " + guess)

if (secret_number == guess_int):
    print("your answer is correct")
else:
    print("you answer is incorre")
    