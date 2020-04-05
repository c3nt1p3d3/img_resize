import csv

# UNFINISHED PROJECT BEWARE, IT'S STILL IN THE MAKING!!!!!!

w = csv.writer(open("output.csv", "w"))
for key, val in dict.items():
    w.writerow([key, val])


database = open("database.txt", "w+")
db = database.readlines()

def check_db():
    # we loop through the Usernames[] list and check for each name in the list
    for user in db:
        if temp_uname == name:
            # then we check if the password that corresponds to the position
            # we have currently selected in the Usernames list is the same as
            # the one we have collected from the input
            if Passwords[Usernames.index(name)] == temp_pass:
                return("Login successful!!")
            else:
                return("Wrong password for the user %s" % (name))
    return(False)


def create_user():
    answer = input("Would you like to create a new account? (yes or no): ")
    if answer == "yes":
        new_user = input("Provide a username: ")
        new_pass = input("Provide a password: ")
        Usernames.append(new_user)
        Passwords.append(new_pass)
        u = open("users.txt", "a")
        u.write(new_user + "\n")
        u.close()
        p = open("passwords.txt", "a")
        p.write(new_pass + "\n")
        p.close()
        return("Account created successfully %s !!!" % (new_user))
    else:
        return("OK, goodbye!!")


temp_uname = input("Username: ")
temp_pass = input("Password: ")

if check_password() == False:
    print("The user doesn't exist!!")
    print(create_user())
else:
    print(check_password())

# Si no quisiéramos imprimirlo, podríamos guardarlo en un array como este:
# result = check_password(temp_pass)
