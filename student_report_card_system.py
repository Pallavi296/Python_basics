class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks=marks


    def display_student_info(self):
        print(f"Name :{self.name}")
        print(f"rollno = {self.rollno}")
        print(f"Marks:")

        for subject, mark in self.marks.items():
            print(f"{subject}:{mark}")

    def calculate_percentage(self):
        total = sum(self.marks.values())
        percentage = total/len(self.marks)
        return percentage

    def grade(self):
        percent = self.calculate_percentage()
        if 90<= percent <=100:
            print("Outstanding")

        if  80<= percent<90:
            print ("Better")

        if 70<=  percent <80:
            print("good")



marks ={"Python":90,"Maths":99,"English":99}
st = Student("Pallavi",789,marks)
st.display_student_info()
print(st.calculate_percentage())
st.grade()

        
    


