## Coded by Sukrut 
input_list = [1,2,[3,4],5,6,7,[8,[9,10]],11]

def sublist1(lst):
	if any(type(r) == list for r in lst) == False:
		return [r+1 for r in lst]              #add 1 to the final list 
	else: 
		list1 = []                             #empty list so that we can later append to it 
		for r in lst:
			if isinstance(r, list):            #checking the nested list 
				for t in r:
					list1.append(t)         #appending value to the empty list 
			else:
				continue              
	return sublist1(list1)                  #returning function so that recursion takes place                      
                       
print(sublist1(input_list))
