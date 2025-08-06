from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship

# Database URL
db_url = "postgresql://postgres:1234@localhost:5432/mydatabase"
engine = create_engine(db_url)

Base = declarative_base()

# Association table for many-to-many: users <-> groups
# #Relational databases (like PostgreSQL) don’t support direct many-to-many relationships — they neeed join/association table to connect them.
user_group = Table(
    'user_group',         #name of the join table
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('group_id', ForeignKey('groups.id'), primary_key=True)
)


# User Table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    # One-to-one relationship
    profile = relationship('Profile', back_populates="user", uselist=False)  #uselist:access only a single object instead of list ,strictly for one-to-one

    # One-to-many relationship
    posts = relationship('Post', back_populates="user")

    # Many-to-many relationship
    groups = relationship('Group', secondary=user_group, back_populates="members")


# Profile Table (One-to-One with User)
class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    bio = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='profile')


# Post Table (One-to-Many with User)
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='posts')

# -------------------------
# Group Table (Many-to-Many with User)
class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    members = relationship('User', secondary=user_group, back_populates='groups')     #It links the relationship from one model to another.

# Create all tables
Base.metadata.create_all(engine)
