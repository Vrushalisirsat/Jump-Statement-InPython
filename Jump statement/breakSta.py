# JUMP Statements :-
# 1) break :- It is used to program control out of the loop before the loop condition becomes false.

# Examples-1 :- using for loop
'''
#__main__

i=1
while i<=5:
    print(i)
    break
    i=i+1
#end of loop
print("Compilers")
#end of __main__

'''

# Examples-2 :- using for loop

#__main__

for i in range(1,6,1):
    print(i)
    if i==2:
      break
      i=i+1
#end of for in loop
print("compiler")
#end of __main__

