import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

hostname = 'mkaws.c13ru45axoez.us-east-2.rds.amazonaws.com'
port = '5432'
db_name = 'statsmk'
username = 'mexico'
password = 'Subway01!'

engine = create_engine('postgresql://' + username + ':' + password + '@' + hostname + ':' + port + '/' + db_name, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()