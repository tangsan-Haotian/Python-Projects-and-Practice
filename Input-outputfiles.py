#this file is  being used  to understand file handling in python

# f=open("sample.txt","r")  #if we didnt set the mod then Sytem will asume that its in read mode
# data=f.read()
# print(data)
# print(type(data)) # this will only functionale if we sre using it in 
# 
# 
# system not online 


#this is the manual method to open and close the file in proper way 
file= open("Dictionary.py", "r") 
content = file.read()
print(content)
file.close()


#this automaticly close file and then suggest the best output regarding it 

# with open("functions.py", "r") as file:
#     content = file.read()
#     print(content)



#to write in any file and replace the main this that may be you attain it 
# file = open("text.txt", "w")

# file.write("Hello Zain, this is my text file.\n")
# file.write("Python file handling is easy!")

# file.close()


with open("text.txt","r") as file:
    content=file.read()
    print(content)