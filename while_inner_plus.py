#Q1 
def q1(lst):
    while any(type(x) == list for x in lst): #if any of the elements in the list are also lists (nested) then enter loop
        x = 0 #start iterator
        replace_list = [] #new list for nested lists
        while x < len(lst): 
            if type(lst[x]) == list: #if that element is a list
                y = 0 #new iterator for nested lists
                while y < len(lst[x]):
                    replace_list.append(lst[x][y]) #apend nested lists to new list 
                    y += 1 #iterate through nested list
                x += 1 #iterate through list
            else:
                x += 1 #do nothing and iterate through list
        lst = replace_list.copy() #chaning list to list of nested lists       
    z = 0 #once out of loop, start counter for adding 1
    while z < len(lst):
        lst[z] += 1 #adding one to each element in final list
        z += 1
    return lst
input_list = [1,2,[3,4],5,6,7,[8,[9,10]],11]
q1(input_list)
