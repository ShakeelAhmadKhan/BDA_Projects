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

def Question_05():
    """
    Q5. Create a program that converts temperature from Farenheit to Celcius or from Celcius to Farenheit.
        Prompt for the starting temperature.
        The program should prompt for the type of conversion and then perform the covnersion.

        The Formulas are
            C = (F-32) x 5/9

            and

            F = (C x 9/5)+32

        Example Output:

        Press C to convert from Farenheit to Celcius.
        Press F to convert from Celcius to Farenheit.
        Your choice: C

        Please enter the temperature in Farenheit: 32
        The temperature in Celcius is: 0.
    """
    TempType = input(" Press C to convert from Farenheit to Celcius.\n Press F to convert from Celcius to Farenheit.")

    if TempType == "C" or TempType == "F":
        print("Your choice: " + TempType)

        if TempType == "C":
            temperature = input("Please enter the temperature in Farenheit: ")
        elif TempType == "F":
            temperature = input("Please enter the temperature in Celcius: ")

        if is_float(temperature) == True:
            if TempType == "C":
                calculatedTemp = (float(temperature) - 32) * 5 / 9
                print("The temperature in Celcius is: " + str(calculatedTemp))
            else:
                calculatedTemp = (float(temperature) * 9 / 5) + 32
                print("The temperature in Farenheit is: " + str(calculatedTemp))
        else:
            print("Invalid temperature entered.")
    else:
        print("Wrong character entered.")
