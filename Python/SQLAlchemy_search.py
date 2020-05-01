import sqlalchemy as db
import sys

# you have to execute this in your console:
# pip install sqlalchemy

# root without password

engine= db.create_engine('mysql+mysqlconnector://root:@localhost/')

connection= engine.connect()
metadata = db.Metadata()

customers = db.Table('customers',
                      metadata,
                      autoload=True,
                      autoload_with=db)

query = db.select([customers.columns.customerNumber,
             customers.columns.customerName,
             customers.columns.phone,
             customers.columns.postalcode,
             customers.columns.country].where(customers.columns.customerName=="%s"%(sys.argv[1])))

ResponseProxy= connection.execute(query)

for r in ResponseProxy.fetchall():
  print(r)
