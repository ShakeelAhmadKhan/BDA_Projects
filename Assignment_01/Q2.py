def is_float(x):
    '''
        This function takes a string as parameter and checks whether it is a Number or not (Integer or Float).
    '''
    try:
        # only integers and float converts safely
        num = float(x)
        return True
    except ValueError as e:  # not convertable to float
        return False

def calculate_tax_amount(amount:float, state:str, tax_percentage:float)->float:
    return float(amount) / 100 * float(tax_percentage)


def take_order_amount() -> str:
    int_count = 0
    str_return = ''

    str_order_amount_query_actual = 'What is the order amount? '
    str_order_amount_invalid = "Order amount entered is invalid. Please enter again.\n"

    # Keep on prompting the user for order amount, unless a correct floating point value is entered.
    while is_float(str_return) == False:
        # if user is bein gprompted for first time then do not cocatenate the string ""
        if int_count > 0:
            str_return = str_order_amount_invalid + str_order_amount_query_actual
        else:
            str_return = str_order_amount_query_actual

        str_return = input(str_return)
        int_count += 1

        return str_return


def take_order_state() -> str:
    str_order_state_query_actual = 'What is the state? '
    str_order_state_invalid = "State entered is invalid. Please enter again.\n"

    int_count = 0
    str_return = ''

    # Keep on prompting the user for state, unless a correct value is etered.

    # Following are the conditions of the correct State
    # 1. Length must be 2 characters
    # 2. Only alphabets must be contained in the State
    int_count = 0
    while len(str_return) != 2 or str_return.isalpha() == False:
        # print ("len(param_order_state):" + str(len(param_order_state)))
        # print ("param_order_state.isalpha(): " + str(param_order_state.isalpha()))
        # if user is bein gprompted for first time then do not cocatenate the string ""
        if int_count > 0:
            str_return = str_order_state_invalid + str_order_state_query_actual
        else:
            str_return = str_order_state_query_actual

        str_return = input(str_return)
        int_count += 1

    return str_return


def Question_02():
    """
    Q2. Write a program to compute the tax on an order amount. The program should prompt
        for the order amount and the state. If the state is “WI,” then the order must be charged
        5.5% tax. The program should display the subtotal, tax, and total for Wisconsin residents
        but display just the total for non-residents.

        Example Output
            What is the order amount? 10
            What is the state? WI

            The subtotal is $10.00.
            The tax is $0.55.
            The total is $10.55.

         Or

            What is the order amount? 10
            What is the state? MN

            The total is $10.00
    """
    tax_percentage = 5.5

    # 1. Get Order amount
    param_order_amount = take_order_amount()

    # 2. Get State
    param_order_state = take_order_state()

    # if state !='WI':
    if param_order_state.find("WI") < 0:
        tax_percentage = 0.0

    # 3. Get the Tax amount calculated
    tax_amount = calculate_tax_amount(param_order_amount, param_order_state, tax_percentage)

    print("The total is $" + str(float(param_order_amount) + float(tax_amount)))
    print("-- ... Question # 02 Ends here ... --")