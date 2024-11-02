import re
def password_strength():
    levels = re.findall (0:"^S{8,}$",
        1:"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
        2:"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$",
        3:"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")

user_password = input("Please enter your password: ")

if user_password == 0:
    print(f"Your password '{user_password}', complies to level {levels}. ")
elif user_password == 1:
    print(f"Your password '{user_password}', complies to level {strength_levels}. ")
elif user_password == 2:
    print(f"Your password '{user_password}', complies to level {strength_levels}. ")
else:
    print(f"Your password '{user_password}', complies to level {strength_levels}. ")