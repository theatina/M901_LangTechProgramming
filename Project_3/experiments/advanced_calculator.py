import numpy as np

class MathError(Exception):
    pass


def input_parser(math_expression):
    operators_list = ["+","-","/","*"]

    user_input_list = math_expression.split(" ")
    while "" in user_input_list:
        user_input_list.remove("")

    corrected_math_expression = " ".join(user_input_list)

    params_given = len(user_input_list)
    if params_given!=5:
        raise MathError(f"\nYou must enter five (5) parameters !\n({params_given} given )\n\nSyntax: <number_1> <operator_1> <number2> <operator_2> <number_3> \n")
    
    else:

        for i in range(0,params_given,2):
            try:
                temp_num = float(user_input_list[i])
                user_input_list[i] = temp_num
            except:
                raise MathError("\nThe first, third and fifth parameters must be integer / floating point numbers !\n")  
        
        user_op_list = [i for i in user_input_list if i in operators_list]
        check_ops = len(user_op_list) == np.ceil(params_given/2)-1

        if check_ops==False:
            raise MathError(f"\nYou have either entered an invalid mathematical operator or misplaced a valid one!\n(valid operators: {operators_list})\n\nSyntax: <number_1> <operator_1> <number2> <operator_2> <number_3>\n")  
    
            
        return corrected_math_expression, 9, user_input_list

calculation_counter = 0
def calculate(n1,op,n2):
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
        if n2==0:
            raise MathError("\nCannot devide with zero ! \n")
        else:
            res = n1/n2
            print(f"{calculation_counter}. {n1} {op} {n2} = {res}")
            return res


def adv_calculator(user_nums_ops_list):
    nums_ops_list = user_nums_ops_list.copy()
    # nums_ops_list = user_nums_ops_list
    
    if len(nums_ops_list)==3:
        n1,op,n2 = nums_ops_list
        return calculate(n1,op,n2)
    
    else:
        pos_of_priority_op = len(nums_ops_list)

        if ("*" in nums_ops_list):
            pos_of_priority_op = nums_ops_list.index("*")
        
        if ("/" in nums_ops_list):
            pos_of_priority_op_div = nums_ops_list.index("/")
            if pos_of_priority_op_div < pos_of_priority_op:
                pos_of_priority_op = pos_of_priority_op_div
        
        if pos_of_priority_op > 1:
            nums_ops_list.insert(2, adv_calculator( nums_ops_list[2:] ) )
            return adv_calculator( nums_ops_list[:3] )
        else:
            nums_ops_list.insert(3, adv_calculator( nums_ops_list[:3] ) )
            return adv_calculator( nums_ops_list[3:] )
 


if __name__=="__main__":

    program_running = True
    while (program_running):

        user_input = input("\nInsert a mathematical expression (use space to separate numbers and operators): \n(type exit to quit \"Advanced Calculator\")\n> ")
        
        if user_input=="exit":
            print(f"\n\nThank you for using \"Advanced Caclulator\"\n\n")
            program_running = False
            break

        try: 
            math_expression,check_input, nums_ops_list = input_parser(user_input)
            calculation_counter = 0
            result = adv_calculator(nums_ops_list)
            print(f"\n{math_expression} = {result}\n")
        
        except MathError as math_err:
            print(f"{math_err.args[0]}")
        