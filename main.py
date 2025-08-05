from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, event
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.engine import Engine

# Database setup
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/students_db"
engine = create_engine(DATABASE_URL, echo=True)  # Automatically prints raw SQL

Base = declarative_base()       # base parent class

# Event listener to show raw query explicitly
@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    print("\nExecuting SQL:\n", statement)
    print("With Parameters:", parameters)

# Department table
class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Backref for reverse access
    students = relationship("Student", back_populates="department")

# Student table
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.id"))

    # Relationship to join with department
    department = relationship("Department", back_populates="students")

# Create tables
Base.metadata.create_all(bind=engine)

# Session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Functions to insert data
def create_department(name):
    dept = Department(name=name)
    session.add(dept)
    session.commit()
    print(f" Department added: {name}")

def create_student(name, age, department_id):
    student = Student(name=name, age=age, department_id=department_id)
    session.add(student)
    session.commit()
    print(f"Student added: {name}, Age: {age}, Dept ID: {department_id}")

# JOIN: Read students with their departments
def read_students_with_department():
    results = session.query(Student).join(Department).all()
    print(" Students and their departments:")
    for s in results:
        print(f"{s.name} ({s.age}) -> {s.department.name}")


create_department("Computer Engineering")
create_department("Electronics")

create_student("Pallavi", 22, 1)
create_student("Kajal", 21, 2)

# --- Perform JOIN query ---
read_students_with_department()
