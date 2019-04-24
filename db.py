import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

hostname = 'ec2-54-83-205-27.compute-1.amazonaws.com'
port = '5432'
db_name = 'd5cnd0ilovske'
username = 'jyciclzpojvtgi'
password = 'da79a5ef5f49f78a84a52cacb7bae615922f31725cb26ec9fde11b9946820970'

engine = create_engine('postgresql://' + username + ':' + password + '@' + hostname + ':' + port + '/' + db_name, echo=True)

Session = sessionmaker(bind=engine)
session = Session()