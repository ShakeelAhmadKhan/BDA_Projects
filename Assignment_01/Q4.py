
def Question_04():
    """
    Q4. Write a program that asks the user for their age and compare it to the legal driven age of sixteen.
        If the user is sixteen or older, then the program should display 'You are old enough to legally drive.'
        If the user is under sixteen, the program should display 'You are not old enough to legally drive.'
    """
    age = input("What is your age? ")

    if str.isdigit(age) == True:
        if int(age) < 16:
            print("You are not old enough to legally drive.")
        else:
            print("You are old enough to legally drive.")
    else:
        print("Invalid age entered.")