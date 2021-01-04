'''
 
Kylafi Christina-Theano
LT1200012

'''

import numpy as np
import argparse

class MathError(Exception):
    pass

def input_parser(math_expression, mode):
    '''
    Makes a number of checks on the math_expression entered by the user, such as validation of operators, int / float numbers and number of given parameters.

    Parameters:     math_expression: list
                    The mathematical expression entered by the user
                    
                    mode: int (1 or 2)
                    1 indicates project's 3 task of advanced calculator supporting a max number of 2 mathematical calculations (5 parameters), while mode 2, supports unlimited calculations

    Returns:        corrected_math_expression: string
                    In case it contains spaces, the "math_expression" is corrected and returned 

                    user_input_list: list
                    List of the given parameters to pass to the advanced_calculator() function for the calculations

    '''

    operators_list = ["+","-","/","*"]

    #User input cleaning of spaces
    user_input_list = math_expression.split(" ")
    while "" in user_input_list:
        user_input_list.remove("")

    corrected_math_expression = " ".join(user_input_list)    
    params_given = len(user_input_list)

    #In case of mode 1 - exercise - the parameters have to be exactly 5
    condition = params_given != 5
    err_msg = f"\nYou must enter five parameters !\n({params_given} given )\n\nSyntax: <number_1> <operator_1> <number2> <operator_2> <number_3> \n"

    #As explained above, in mode 2, the parameters just have to be at least 3 and not odd in number, because that means there is something wrong with the input - not a valid mathematical expression
    if mode == 2:
        condition = params_given < 3 or params_given % 2==0
        err_msg = f"\nInvalid Syntax: {params_given} parameters were given\n\nSyntax: <number_1> <operator_1> ... <operator_N-1> <number_N> (N = 2k+1, where k positive integer -> k >= 1)\n"

    #The aforementioned conditions raise the MathError exception with the respective message 
    if condition:
        raise MathError(err_msg)
    
    else:
        #Performing a check of the numbers of the mathematical expression to be integer or float, in the correct positions and raising the MathError exception in case of an error
        for i in range(0, len(user_input_list), 2):
            try:
                temp_num = float(user_input_list[i])
                user_input_list[i] = temp_num
            except ValueError:
                raise MathError("\nThe parameters with index 2k, must be integer / floating point numbers\n")   
        

        #Checking that the valid operators given are exactly 1 less in number than the int/float numbers given 
        user_op_list = [i for i in user_input_list if i in operators_list ]
        if len(user_op_list)==0:
            raise MathError(f"\nYou have not entered any (valid) operators !\n")  

        elif len(user_op_list) != np.ceil(params_given/2)-1:
            raise MathError(f"\nYou have entered an invalid mathematical operator !\n(valid operators: {operators_list})\n") 

        
        #Encorporate the minus sign (-) in the numbers and then change it to plus sign (+), for future caclulations 
        #(subtraction of a number is the addition of its negative -> n1 - n2 = n1 + (-n2)
        for i in range(1,len(user_input_list),2):
            if user_input_list[i]=="-":
                user_input_list[i]="+"
                user_input_list[i+1]*= -1

        return corrected_math_expression, user_input_list


#global counter of calculations for printing the calculation steps
calculation_counter = 0
def calculate(n1,op,n2):
    '''
    Calculates the mathematical expression "n1 (+,-,/,*) n2", using the parameters given 

    Parameters:     n1: int or float
                    The first integer of floating point nunmber of the expression
                    
                    op: "+" or "-" or "/" or "*"
                    Operator of the expression

                    n2: int or float
                    The first integer of floating point nunmber of the expression

    Returns:        res: float
                    The result of the calculation

    '''

    global calculation_counter
    if calculation_counter == 0:
        print("\nCalculations:\n")
    calculation_counter+=1

    if op=="+":
        res = n1+n2
        print(f"{calculation_counter}. {n1} {op} {n2} = {res}")
        return res
    elif op=="-":
        res = n1-n2
        print(f"{calculation_counter}. {n1} {op} {n2} = {res}")
        return res
    elif op=="*":
        res = n1*n2
        print(f"{calculation_counter}. {n1} {op} {n2} = {res}")
        return res
    else:
        #Check for 0 division which is not permitted
        if n2==0:
            raise MathError("\nCannot devide with zero ! \n")
        else:
            res = n1/n2
            print(f"{calculation_counter}. {n1} {op} {n2} = {res}")
            return res

def adv_calculator(user_nums_ops_list):
    '''
    Recursive function that calculates mathematical expressions of more than 1 calculations, supporting unlimited calculations and operator priority. For each call, checks if the first operator of the input expression must be given priority and returns the proper result, calling itself recursively, till 3 parameters are left and the final result is returned. 

    Parameters:     user_nums_ops_list: list
                    List of the total parameters given by the user (all numbers and operators)

    Returns:        result: float
                    The result of all the calculations in the mathematical expression of the user

    '''

    # nums_ops_list = user_nums_ops_list.copy()
    nums_ops_list = user_nums_ops_list
    
    #Termination condition of the recursive function - when 3 parameters are left, the calclulate() function is called, to return the final calculation
    if len(nums_ops_list)==3:
        n1,op,n2 = nums_ops_list
        return calculate(n1,op,n2)
    
    else:
        #Let the first operator be + or -
        first_is_priority_op = False

        #If the operator is * or /, then it is a priority operator
        if ( set(nums_ops_list[1]).issubset(set(["*","/"]))):
            first_is_priority_op = True
        
        #If the first operation of the expression has priority, it is calculated first, it is inserted in the user nums_ops_list (expression of the respective function call) as a substitute of the 3 parameters of the first calculation and then the rest of the operations are calculated through the recursive call of the function
        if first_is_priority_op:
            nums_ops_list.insert(3, adv_calculator( nums_ops_list[:3] ) )
            return adv_calculator( nums_ops_list[3:] )
       
        else:
            #If the first operation is not a priority one, the recursive function is called for the rest of the operations first, and then for the last 3 parameters, including the first number, first operator and the result of the aforementioned calculations
            nums_ops_list.insert(2, adv_calculator( nums_ops_list[2:] ) )
            return adv_calculator( nums_ops_list[:3] )


if __name__=="__main__":

    #The user can choose between 2 modes, by using argument " --mode < 1 or 2 > "
    # --mode 1: Exercise mode, supporting 5 parameters ( 2 calculations )
    # --mode 2: Unlimited calculations mode, supporting unlimited calculations
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=int, default='1')
    args = parser.parse_args()

    if args.mode == 2:
        print(f"\n --> UNLIMITED CALCULATIONS MODE... ON ! <--\n")
    
    program_running = True
    while (program_running):

        user_input = input("\nInsert a mathematical expression (use space to separate numbers and operators): \n(type exit to quit \"Advanced Calculator\")\n> ")
        
        if user_input=="exit":
            print(f"\n\nThank you for using \"Advanced Caclulator\"\n\n")
            program_running = False
            break

        try: 
            corrected_math_expression, nums_ops_list = input_parser(user_input, args.mode)
            calculation_counter = 0
            result = adv_calculator(nums_ops_list)
            print(f"\n{corrected_math_expression} = {result}\n")
        
        except MathError as math_err:
            print(f"{math_err.args[0]}")

