import os
raw_original=input("Enter the expression with space: ")
print("your Input is: "+raw_original)
original=raw_original.split(" ")
num=[]
sign=[]
flag=0
flag=0
for i in original:
    issign=True if i=='+' or i=='-' else False
    isnum=False
    if(issign==False):
        isnum= True if int(i)<=9 or int(i)>=0 else False
    if(isnum and issign==False):
        if(int(original[flag])<9 and int(original[flag])>0):
            num.append(int(original[flag]))
            flag+=1
    else:
        sign.append(original[flag])
        flag+=1

if len(num)!=(len(sign)-1):
    print("You entered a wrong expression. Please make sure it is a mathematical expression...")


print("Your Postfix expression is: "+str(num)+" "+str(sign))


