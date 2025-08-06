from sqlalchemy.orm import sessionmaker
from models import User, Profile, Group, Post, engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data (optional, for testing)
session.query(Group).delete()
session.query(Post).delete()
session.query(Profile).delete()
session.query(User).delete()
session.commit()

#  Add users
users = [
    User(name="Pallavi", age=23),
    User(name="Kajal", age=25),
    User(name="Krish", age=20),
    User(name="Max", age=27)
]
session.add_all(users)
session.commit()

# Fetch users from DB
pallavi = session.query(User).filter_by(name="Pallavi").first()
kajal = session.query(User).filter_by(name="Kajal").first()
krish = session.query(User).filter_by(name="Krish").first()
max_user = session.query(User).filter_by(name="Max").first()

# Add profiles
profile1 = Profile(bio="Hello!I’m Pallavi!", user=pallavi)
profile2 = Profile(bio="I'm Kajal... Passionate about AI.", user=kajal)
profile3 = Profile(bio="Krish here. Python dev!", user=krish)
profile4 = Profile(bio="Max the backend king!", user=max_user)
session.add_all([profile1, profile2, profile3, profile4])
session.commit()

#  Add groups and assign users
admin_group = Group(name="Admin", members=[pallavi, kajal])
dev_group = Group(name="Developer", members=[krish, max_user])
session.add_all([admin_group, dev_group])
session.commit()

#  Add posts for each user
post1 = Post(title="SQLAlchemy Basics", user=pallavi)
post2 = Post(title="Advanced FastAPI", user=kajal)
post3 = Post(title="Docker Mastery", user=krish)
post4 = Post(title="PostgreSQL Tips", user=max_user)
session.add_all([post1, post2, post3, post4])
session.commit()

# Print user data
users = session.query(User).all()
for user in users:
    print(f"Name: {user.name}, Age: {user.age}")
    print(f"Profile: {user.profile.bio if user.profile else 'No profile'}")
    print(f"Posts: {[post.title for post in user.posts]}")
    print(f"Groups: {[group.name for group in user.groups]}")
