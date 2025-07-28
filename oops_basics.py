class Employee:
    def __init__(self,type,name,age,city,salary):

        self.type=type
        self.name=name
        self.age=age
        self.city=city
        self.salary=salary

    def show(self):
        print(f"The Emplyees {self.type},{self.name},{self.age},{self.city},{self.salary}")
emp = Employee("self-Employee","Pallavi",23,"Ahemdabad",9000000)
emp.show()

    
