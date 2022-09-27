input_list = [1,2,3,4,[5,6,7,[8,9,]]]

list1 = input_list
ind = 0

while True:
  length = len(list1)           #assigning variable the length of list 
  if type(list1[ind]) == list:  #comparing if both the types are same 
    list1 = list1[ind]          #using indexing, we assign the value to list 
    ind = 0                     #assigning ind the value of 0 so that the counting starts from 0 
  else:
    ind += 1                    #iterating the value of ind by 1  
  if ind == length:             #if ind is same as length of the list, then only it will break 
  	break

add = [x+1 for x in list1]      #using list comprehension to add 1 to the list
print(add)
