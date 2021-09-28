#general approach to image file processing.
import shutil
import os
flag=0
if flag==0:
    target=os.path.relpath(input("Enter file name: "))                             #takes relative path
    flag4=os.path.exists(target)
    if flag4==True:
        b=int(input("1)Save 0)To exit: "))
        original=os.path.relpath(os.getcwd(),input("Enter real path where you want to store the file: "))
        if b==1:
            flag3=os.path.exists(os.path.realpath(original))
            if flag3==True:
                target=os.path.relpath(os.getcwd(),input("Enter the folder name relatively: "))
                flag2=shutil.move(original,target)
                if(flag2==True):
                    print("Move Succesfull. Thank you for your help.")
                    flag=False
                else:
                    print("Try again...... Some error has occured. Either the file does not exist or has been moved....")
            else:
                flag=True
    else:
        print("File does not exists in the current folder..")
elif flag==True:
    flag=False
else:
    print("Error in input. Try Again")

