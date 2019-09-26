def verification():
    username = input("Input you username: ")
    password = input("Input your password: ")

    user1 = input("Username: ")
    pass1 = input("Password: ")

    if username != user1:
        print("Invalid Username")
    elif password != pass1:
        print("Invalid Password")

    else:
        print("Access Granted!!")


verification()
