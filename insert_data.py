from sqlalchemy.orm import sessionmaker
from models1 import engine, Customer, Order

Session = sessionmaker(bind=engine)
session = Session()

# Clean previous data
session.query(Order).delete()
session.query(Customer).delete()
session.commit()

# Add Customers
cust1 = Customer(name="Riya", email="riya@example.com")
cust2 = Customer(name="Bob", email="bob@example.com")

# Add Orders
order1 = Order(product="Laptop", amount=90000, customer=cust1)
order2 = Order(product="Phone", amount=30000, customer=cust1)
order3 = Order(product="Tablet", amount=20000, customer=cust2)

# Save to DB
session.add_all([cust1, cust2, order1, order2, order3])
session.commit()

print("Sample data inserted.")
