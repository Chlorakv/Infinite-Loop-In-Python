#Infinite Loop In Python By Chlorakv.
#In this code I have written a code in which the program won't stop running until the user kills the program. 

#Providing an Initial Value.
n = 1

#Using while loop.
while True:
    
    #Using if statement in which n is greater than 0 then it will start printing numbers
    if n > 0:
        print(n)
        
        #Now n will start printing in the output where the value of n will increase by 1 and it will run as an infinite loop. 
        n += 1