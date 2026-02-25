#this file is  being used  to understand file handling in python

f=open("sample.txt","r")  #if we didnt set the mod then Sytem will asume that its in read mode
data=f.read()
print(data)
print(type(data)) # this will only functionale if we sre using it in system not online 