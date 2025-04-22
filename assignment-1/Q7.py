import random

# Generate a 3-digit lottery number
lottery = ''.join([str(random.randint(0,9)) for _ in range(3)])
lottery = int(lottery)

user = input("Enter a 3-digit number: ")
if not user.isdigit() or len(user) != 3:
    print("Invalid input")
    exit()
user = int(user)

if user == lottery:
    print("$10,000")
else:
    if sorted(str(user)) == sorted(str(lottery)):
        print("$3,000")
    else:
        user_digits = set(str(user))
        lottery_digits = set(str(lottery))
        if user_digits & lottery_digits:
            print("$1,000")
        else:
            print("No award")