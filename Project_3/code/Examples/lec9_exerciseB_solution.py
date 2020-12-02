class MathError(Exception):
    pass


def parse_input(input_text):
    '''
    If the user does not enter three parameters, you must raise a MathError exception
    with the message "You must enter three parameters"
    If the first and last parameters are not int, you must raise a MathError exception
    with the message "The first and third parameters must be int numbers"
    If the second parameter is not a mathematical operator (+, -, * or /)
     you must  raise a MathError exception with the message "You have not entered a valid mathematical operator"
    :param input_text: The input text of the user
    :return: A tuple with string representation of numberA, mathematical_operator, numberB
    '''
    params = input_text.split(" ")
    if len(params) == 3:
        return params[0], params[1], params[2]
    else:
        raise MathError("You must enter three parameters")

def calculate(number_a, operator, number_b):
    '''
    :param number_a: String representation of number a
    :param operator: Mathematical operator as a string
    :param number_b: String representation of number b
    :return:
    '''
    try:
        number_a = int(number_a)
        number_b = int(number_b)
    except ValueError:
        raise MathError("The first and third parameters must be int numbers")
    if operator not in ["+","-","/","*"]:
        raise MathError("You have not entered a valid mathematical operator")
    else:
        if operator == "+":
            return number_a + number_b
        elif operator == "-":
            return number_a - number_b
        elif operator == "*":
            return number_a * number_b
        else:
            return number_a / number_b


while True:
    user_input = input('>>> ')
    if user_input == 'quit':
        break
    try:
        n1, op, n2 = parse_input(user_input)
        result = calculate(n1, op, n2)
    except MathError as e:
        print(e.args[0])
    else:
        print(result)
