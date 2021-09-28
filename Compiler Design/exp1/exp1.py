raw_input=input("Enter the expression with space: ")
print("your Input is: "+raw_input)
original=raw_input.split(" ")
num=[]
sign=[]
counter=0
for i in original:
    issign=True if i=='+' or i=='-' else False
    if(issign==False):
        if(int(i)>=0 and int(i)<=9):
            num.append(int(original[counter]))
            counter+=1
    elif(issign==True):
        sign.append(original[counter])
        counter+=1
    else:
        sign.append(original[counter])
        counter+=1

if len(num)==(len(sign)-1):
    print("You entered a wrong expression. Please make sure it is a mathematical expression...")


print("Output: "+str(num[0])+str(num[1])+str(sign[0])+str(num[2])+str(sign[1]))


