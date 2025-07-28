class Student:
    def details(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def show(self):
        print(f"Name:{self.name}")
        print(f"rollno:{self.rollno}")
        print(f"Marks")
        for subject,mark in self.marks.items():
            print(f"{subject}:{mark}")
            print(f"Percentage:{self.calculate_percentage():.2f}")
            print(f"Grade:{self.grade()}")

    def calculate_percentage(self):
        total = sum(self.marks.values())
        percentage = total/len(self.marks)

    def grade(self):
         percent = self.calculate_percentage()
        
         if 90<= percent <=100:
             return "Outstandig"
         if 80<=percent<90:
             return "Excellent"
         if 70<=percent<60:
             return "Good"
         
student =  []
n = int(input("Enter how many student details you want to enter:"))

for i in range(n):
    print(f"Enter the number of details of the student:{n+1}")
    name=input(f"Enter name:{name}")
    rollno = int(input("Enter rollno:"))
    Subject = input("Enter subject: ")

    marks={}

for j in marks(Subject):
    Subject = input(f"Enter Subject{j+1} name:")
    Marks = int(input("Enter marks:")) 
    Marks[Subject]=mark


    st = Student(name,rollno,marks)
    st.append(Student)
     

    print("Report card:")
    for st in students:
        



        
    