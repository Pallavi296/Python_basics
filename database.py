from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#PostgreSQL database URL format: "postgresql://user:password@host:port/database_name"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345@db:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()   #object of database