# coding: utf-8

import mysqlx

# Connect to server on localhost
session = mysqlx.get_session({'host': 'localhost', 'port': 33060, 'user': 'root', 'password': 'root'})

schema = session.get_schema('test')

# Use the collection 'my_collection'
schema.create_collection('my_collection', True)
collection = schema.get_collection('my_collection')

session.close()
