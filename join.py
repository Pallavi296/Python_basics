from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, join
from models1 import engine, Customer, Order

Session = sessionmaker(bind=engine)
session = Session()

#  INNER JOIN
print("INNER JOIN ")
results = session.query(Customer.name, Order.product).join(Order).all()
for name, product in results:
    print(f"{name} bought {product}")

# LEFT OUTER JOIN
print(" LEFT OUTER JOIN ")
results = session.query(Customer.name, Order.product).outerjoin(Order).all()
for name, product in results:
    print(f"{name} bought {product if product else 'No Orders'}")

#  JOIN with filter
print("JOIN with filter (Laptop orders) --")
results = session.query(Customer.name, Order.product).join(Order).filter(Order.product == "Laptop").all()
for name, product in results:
    print(f"{name} bought {product}")
