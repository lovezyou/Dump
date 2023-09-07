def isLeap(year):                                               #this function is to find the given year is leap or not
	if(year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
		return(True)
	else :
		return(False)



year=int(input("Enter a year : "))                              #the year given by the user is stored in the variable year
if isLeap(year):                                                #the function isLeap() is called by the if condition with the argument "year" 
	print("the year {} is a leap year.".format(year))
else :
	print("the year {} is not a leap year.".format(year))

