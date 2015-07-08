from aboardly import Aboardly

client = Aboardly('9bf33bd9', '41fb938bd2814a9226100dff2e07d4fb')

data = { 'email': 'python@example.com', 'age': 30 }
r = client.customers.upsert("customer_id_new", data)
print r.status_code, r.text

r = client.events.create("customer_id_new", 'foobar')
print r.status_code, r.text
