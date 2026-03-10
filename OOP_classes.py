#this was being created to understand the basics of oops
class student:
    name="zain"
    Cast="solangi"
    number=3078232501

# print(student.name)
#this a blue [print type class that emplifies the details that shows that how the things have properties and what properties have they ]

#this is object by using class attributes by using object we are calling propertises ao classes 
# s1=student()
# print(s1.name)

# s2=student()
# s2.name="Oshaque"
# print(s2.name)
# print(s1.name)

class student:
    name="shazain"
    age="22"
    school="sukkur IBA Public"
    ain="be like Gojo"

#this is constrctor which has been called every time 
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("this is the data for new student")


s1=student("karan","79")
print(s1.name,s1.marks)
print(s1.marks)
        
