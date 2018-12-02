# coding: utf-8

import mysqlx

# Connect to server on localhost
session = mysqlx.get_session({'host': '127.0.0.1', 'port': 33060, 'user': 'root', 'password': 'root'})

try:
    schema = session.get_schema('mysql')
    schema.create_collection('my_collection', True)
    collection = schema.get_collection('my_collection')

    # Start Transaction
    session.start_transaction()

    # INSERT
    record_list = [{"_id": _id, "age": _id * 5} for _id in range(10)]
    collection.add(*record_list).execute()

    # READ
    record = collection.find("age >= :param").bind("param", 21).limit(2).execute()
    for rec in record.fetch_all():
        print(rec)

    # UPDATE
    collection.modify("age <= 21") \
        .patch('{"_is": "young"}').execute()
    collection.modify("age > 21") \
        .patch('{"_is": "old"}').execute()

    # DELETE
    collection.remove("age >= 31").execute()

    # COMMIT
    session.commit()

except Exception:
    # ROLLBACK
    session.rollback()
finally:
    session.close()
