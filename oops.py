#this file is being used to understand the basics and advance concepts of the opps in
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no= acc_no
#         self.acc_pass=acc_pass
#         pass

class Student:
    def __init__(self,name):
        self.name=name

s1=Student("Abbas")

s2=Student("Asad")
print(s1.name)
print(s2.name)
del s2.name

print(s2.name)