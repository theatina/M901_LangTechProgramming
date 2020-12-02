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
    return "","",""

def calculate(number_a, operator, number_b):
    '''
    :param number_a: String representation of number a
    :param operator: Mathematical operator as a string
    :param number_b: String representation of number b
    :return:
    '''
    return 0


while True:
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  n1, op, n2 = parse_input(user_input)
  result = calculate(n1, op, n2)
  print(result)
