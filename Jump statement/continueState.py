# 2) whenever a continue statement is executed,the loop starts its next iteration.

# Examples-1 -> WAP to print all odd numbers from 1 to 5 by using while loop.
'''
# __main__
i=0

while i<5:
    i=i+1
    if i%2 == 0:
        continue
    #end of if
    print(i)
#end of while loop

'''

# Examples-2 -> WAP to print all odd numbers from 1 to 5 by using for-in loop.

# __main__

for i in range(1,6):
    if i%2==0:
        continue
    #end of if
    print(i)
#end of loop
#end of __main__


# 3) pass statement