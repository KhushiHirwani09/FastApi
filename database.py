from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL="postgresql://cadmin:root@localhost:5432/crud"
engine=create_engine(DATABASE_URL)
sessionlocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()
