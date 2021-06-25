
def is_float(x):
    '''
        This function takes a string as parameter and checks whether it is a Number or not (Integer or Float).
    '''
    try:
        # only integers and float converts safely
        num = float(x)
        return True
    except ValueError as e: # not convertable to float
        return False

def Calculate_Simple_Interest(principal_amount: float, time_duration: float, rate_in_percentage: float) -> float:
    print('The Principal Amount is: ', principal_amount)
    print('The Time duration is: ', time_duration)
    print('The Rate of Interest (in percentage) is', rate_in_percentage)

    si = (principal_amount * time_duration * rate_in_percentage) / 100

    print('The Simple Interest is:', str(si))
    return si

def Question_01():
    """
        Q1. Write a program that computes simple interest. Prompt for the principal amount, the
        rate as a percentage, and the time, and display the amount accrued (principal + interest).
        The formula for simple interest is A = P(1 + rt), where P is the principal amount, r is the
        annual rate of interest, t is the number of years the amount is invested, and A is the amount
        at the end of the investment.
        Example Output:
            Enter the principal: 1500
            Enter the rate of interest: 4.3
            Enter the number of years: 4
            “After 4 years at 4.3%, the investment will be worth $1758.”
    """
    # Driver code
    Prin = input("Enter the principal: ")
    if str.isdigit(Prin) == True:
        Rate = input("Enter the rate of interest: ")
        if is_float(Rate) == True:
            Time = input("Enter the number of years: ")
            if str.isdigit(Time) == True:
                print("----------------------------------------------------------------------------")
                Simple_Interest_ = Calculate_Simple_Interest(float(Prin), float(Time), float(Rate))
                # Simple_Interest_ = (Prin * Time * Rate)/100
                print("Sum of Principal Amount and Simple Interest is: " + str(int(Simple_Interest_) + int(Prin)))
            else:
                print("Invalid number of years.")
        else:
            print("Invalid rate of interest.")
    else:
        print("Invalid principal amount.")
    print("-- ... Question # 01 Ends here ... --")