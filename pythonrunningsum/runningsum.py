#Calculating a running sum
#A user will enter numbers that will be added to the sum 
#when a negative number is encountered stop adding numbers 
#write out the final result

sum = 0, -1, 2, 32, 40, 55, -8, 50, -15
number = -10

def sum_cal():
    sum_calculation = int(input('enter the sum: '))
    if sum_calculation < 0 :
        final_sum = number + sum_calculation
        print('the running sum is', final_sum )
    else:
        final_sum = number + sum_calculation
        print('the running sum is', final_sum, 'only negative numbers are required')
sum_cal()        
