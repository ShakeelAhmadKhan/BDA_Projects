
def Question_03():
    """
    Q3. Write a program that validates userlogin credentials.
        The program must prompt the user for a username and password.
        The program should compare the password given by the user to a known password.
        If the password matches, the program should display “Welcome!”
        If it doesn’t match, the program should display “I don’t know you.”

        Example Output
            What is the password? 12345
            I don't know you.
        Or

            What is the password? abc$123
            Welcome!
    """
    str_known_password = "12Password34%"
    print(str_known_password)
    str_user_name = input("Enter User Name: ")
    str_user_pass = input("What is the password? ")

    if str_user_pass == str_known_password:
        print("Welcome!")
    else:
        print("I don’t know you.")
    print("-- ... Question # 03 Ends here ... --")