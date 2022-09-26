def three (arg):						      #defining a function which taken an argument 
	my_list = [1,2,3,4,5,6,7,8,9]		#list which will be used 
	g = [x for x in my_list if x<= arg]	#using list comprehension to count the list till specified argument only 
	print(g)							          #printing the list 

three(5)								          #specifying the argument for the function 
