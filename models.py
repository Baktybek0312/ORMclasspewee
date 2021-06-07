from peewee import *

db = SqliteDatabase("database.db")
db_my = MySQLDatabase('my_db', user='db_user', password='db_pass', host='localhost')
db_psql = PostgresqlDatabase('my_db', user='db_user', password='db_pass', host='localhost')

class Customer(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()

    class Meta:
        database = db
        order_by = 'id'
        db_tables = 'customer'

class Market(Model):
    id = PrimaryKeyField(unique=True)
    products = IntegerField()
    products_date = DateField()
    customer_id = ForeignKeyField(Customer)

    class Meta:
        database = db
        order_by = 'id'
        db_tables = 'market'
