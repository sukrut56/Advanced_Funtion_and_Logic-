input_list = [1,2,3,4,[5,6,7,[8,9,[10, 11]]]]

list1 = input_list

def sublist1(list):
    if(len(list) > 1):              #checking length of list 
        for j in list:              
            if type(j) == type([]) :  #checking type of list 
               return sublist1(j)     #returning the function so that recursion takes place
            else:
                continue              #continue until innermost list is reached
    return list                       #returning the innermost list 

sublist1(list1)                       #executing the function

s = sublist1(list1)
add = [t+1 for t in s]                #adding 1 to the list using list comprehension 
print(add)
