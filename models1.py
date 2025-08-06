from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Customer Table
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    # One-to-many: One customer → many orders
    orders = relationship('Order', back_populates='customer')

# Order Table
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    product = Column(String)
    amount = Column(Integer)

    # Foreign key to customers table
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Many-to-one: Each order → one customer
    customer = relationship('Customer', back_populates='orders')

# Create engine and tables
engine = create_engine('postgresql://postgres:1234@localhost:5432/mydatabase')
Base.metadata.create_all(engine)
