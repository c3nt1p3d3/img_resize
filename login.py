def check_password(temp_pass):
    # we loop through the Usernames[] list and check for each name in the list
    for name in Usernames:
        # if the name we got through input is equal to the name currently selected in the Usernames list
        if temp_uname == name:
            # then we check if the password that corresponds to the position
            # we have currently selected in the Usernames list is the same as
            # the one we have collected from the input
            if Passwords[Usernames.index(name)] == temp_pass:
                return("Login successful!!")
            else:
                return("Wrong password for the user " + name + ", try again!")
    return("Wrong username!!!")

Usernames = ["Admin", "Jorge"]
Passwords = ["KEK", "Mierda"]


temp_uname = input("Username: ")
temp_pass = input("Password: ")

print(check_password(temp_pass))
# Si no quisiéramos imprimirlo, podríamos guardarlo en un array como este:
# result = check_password(temp_pass)
