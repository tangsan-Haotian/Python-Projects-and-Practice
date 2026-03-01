#this file is  being used  to understand file handling in python

# f=open("sample.txt","r")  #if we didnt set the mod then Sytem will asume that its in read mode
# data=f.read()
# print(data)
# print(type(data)) # this will only functionale if we sre using it in 
# 
# 
# system not online 


# #this is the manual method to open and close the file in proper way 
# file= open("Dictionary.py", "r") 
# content = file.read()
# print(content)
# file.close()


#this automaticly close file and then suggest the best output regarding it 

# with open("functions.py", "r") as file:
#     content = file.read()
#     print(content)



#to write in any file and replace the main this that may be you attain it 
# file = open("text.txt", "w")

# file.write("Hello Zain, this is my text file.\n")
# file.write("Python file handling is easy!")

# file.close()


# with open("text.txt","r") as file:
#     content=file.read()
#     print(content)

# f=open("text.txt","r") 

# #  content=f.read()  #if i write read(10) then it would show that the function is gonna print the lines and  10 character of file 
# # content=f.readline(2) #this would print the lines from specific caracter file
# # print(content)

# f.close()


# f = open("text.txt","a+")
# f.seek(0)   # Move pointer to start
# print(f.read())
# f.write(" its me zain here to help you son")
# f.close()

#this read the daata and then implify the result
# with open("text.txt", "r+") as f:
#     data = f.read()
#     print(data)

#modules are like functions that we can use to make a code functionable and reusable till its in need 

# import os
# #OS  is a module that is mostly used to perform 
# with open("practice.txt","w") as f:
#     f.write("iam here to rule this city not to survive in this ")
# #thsi creat the file and then put the data in it 

# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)

# this will return the line number in the text where the  word will be matched

# def check_for_line():
#     word = "zain"
#     line_no = 1
    
#     with open("text.txt", "r") as f:
#         for line in f:
#             if word in line:
#                 return line_no
#             line_no += 1
    
#     return -1


