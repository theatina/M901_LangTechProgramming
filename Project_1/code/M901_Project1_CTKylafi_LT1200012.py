'''

Kylafi Christina-Theano
LT1200012
M901 - Project 1


'''


def find_largest(num_list): 
    '''
    Finds the largest of all the numbers in the given list in a c - wise way (loop's and if's - cases)


    Parameters:     num_list: list of numbers (integers and floats)
    
    Returns:        max_num: number with the maximum value in the num_list

    '''

    # checks if list is empty
    if len(num_list)>1:
        # returns maximum number of all the numbers in the given list
        max_num = num_list[0]
        for i in num_list[1:]:
            if i > max_num:
                max_num = i
        return max_num
    
    elif len(num_list)==1:
        return num_list[0]
   
    else:
        # print("\nList must have at least 1 number ! !\n")
        return None



def find_largest_from_the_two(num_list1, num_list2): 
    '''
    Finds the largest of all the numbers in the two given lists by using function find_largest()


    Parameters:     num_list1: first list of numbers (integers and floats)
                    num_list2: second list of numbers (integers and floats)
    
    Returns:        max_num: the number with the greatest value in both num_list1 and num_list2

    '''
    
    #finds the max number of each list 
    max1 = find_largest(num_list1)
    max2 = find_largest(num_list2)

    # if there is at least 1 non-empty list, the respective max is not None
    if max1!=None or max2!=None:
        
        # checks the values of max numbers
        # if list 1 was empty then the max number of the two lists is the max number of list 2
        if max1==None:
            return max2

        # if list 1 was empty then the max number of the two lists is the max number of list 2
        elif max2==None:
            return max1
        
        # if both lists were non empty, then the functions returns the max of the two max numbers, 
        # which could have been done by comparing their values and choosing the greater
        else:
            max_num = max(max1,max2)
            return max_num

    # both lists were empty so both variables have None value - no max number to return
    else:
        return None



# The following functions are augmentations of the two functions above, producing the same outcome in a different way, 
# with more input checks and no use of loops

# augmented / extended versions of the two functions above
def find_largest_version2(num_list=None, *args): 
    '''
    Finds the largest of all the numbers in the given list


    Parameters:     num_list: list of numbers (integers and floats)
    
    Returns:        maximum of the numbers in the num_list

    '''

    # checks number of given arguments to inform the user in case of error by using the variable length argument feature 
    # and default value feature of python functions
    if num_list==None:
        print("\n--> Function: find_largest_version2()\n\nERROR: find_largest_version2() takes exactly one argument(none were given)\n")
        return None
    elif len(args)>0:
        print("\n--> Function: find_largest_version2()\n\nERROR: find_largest_version2() takes exactly one argument (2 or more were given)\n")
        return None

    # checks if given list is empty
    if len(num_list)>0:
        # returns maximum number of all the numbers in the given list
        return max(num_list)
    else:
        print("\n--> Function: find_largest_version2()\n\nList must have at least 1 number ! !\n")
        return None



def find_largest_from_the_two_version2(num_list1=None, num_list2=None, *args): 
    '''
    Finds the largest of all the numbers in the two given lists


    Parameters:     num_list1: first list of numbers (integers and floats)
                    num_list2: second list of numbers (integers and floats)
    
    Returns:        maximum of the numbers in both num_list1 and num_list2 

    '''

    # checks number of given arguments to inform the user in case of error by using the variable length argument feature 
    # and default value feature of python functions
    if num_list1==None or num_list2==None:
        print("\n--> Function: find_largest_from_the_two_version2()\n\nERROR: find_largest_from_the_two_version2() takes exactly two arguments (1 or less were given)\n")
        return None
    elif len(args)>0:
        print("\n--> Function: find_largest_from_the_two_version2()\n\nERROR: find_largest_from_the_two_version2() takes exactly one argument (3 or more were given)\n")
        return None

    # checks if both lists are empty
    if len(num_list1)==0 and len(num_list2)==0:
        print("\n--> Function: find_largest_from_the_two_version2()\n\nAt least 1 list must have at least 1 number ! !\n")
        return None
    else:
        # creates a new list of all the elements in the two given lists, to find the greater value between them all
        # if a list is empty, then the max number of the non empty list is returned
        num_list = []
        num_list.extend(num_list1)
        num_list.extend(num_list2)
        return max(num_list)



# testing of function find_largest()
num_list = [9,3,4,6,-1,3,-10,-4.3,12.33,99]    
a = find_largest(num_list)
if a is not None:
    print("\n--> Function: find_largest()\n\nA) Largest number of list %s : %s\n"%( num_list , str(a) ))

# testing of function find_largest_from_the_two()
list1 = [10.3,7.4,9,2,5,-1,0]
list2 = [99,0.3,1010.3,8]
b = find_largest_from_the_two(list1,list2)
if b is not None:
    print("\n--> Function: find_largest_from_the_two()\n\nB)\nList1 = %s \nList2 = %s\n\nLargest number of lists: %s\n\n"%( list1, list2 , str(b) ))


# testing of version2 functions
# testing of function find_largest_version2()
num_list = [73,5,6,7,10,3,34]    
a_2 = find_largest_version2(num_list)
if a_2 is not None:
    print("\n--> Function: find_largest_version2()\n\nA) Largest number of list %s : %s\n"%( num_list , str(a_2) ))

# testing of function find_largest_from_the_two_version2()
list1 = [6,-49,9,1,19,23.42,2,34,-199]
list2 = [99,-0.3,21.9,8]
b_2 = find_largest_from_the_two_version2(list1,list2)
if b_2 is not None:
    print("\n--> Function: find_largest_from_the_two_version2()\n\nB)\nList1 = %s \nList2 = %s\n\nLargest number of lists: %s\n\n"%( list1, list2 , str(b_2) ))