
from models import *
import datetime

with db:

    # pokupatel2 = Customer.create(name='Kayrat')
    # print(pokupatel2)
    # pokupatel3 = Customer.insert(name='Bektur').execute()
    # print(pokupatel3)
    # pokupatel1 = Customer(name='Baha').save
    # print(pokupatel1)
    # pokupatel = Customer.select()
    # globus = [
    #     {'products': 2,'products_date':datetime.date(2021, 6, 4),'customer_id':pokupatel[0]},
    #     {'products': 1,'products_date':datetime.date(2021, 6, 4),'customer_id':pokupatel[1]},
    #     {'products': 3,'products_date':datetime.date(2021, 6, 4),'customer_id':pokupatel[2]},
    #     {'products': 5,'products_date':datetime.date(2021, 6, 4),'customer_id':pokupatel[4]},
    # ]
    # Market.insert_many(globus).execute()

    pokup = Customer.get(Customer.id == 2)
    print(pokup.id, pokup.name)

    prod = Market.select().where(Market.customer_id == 3)

    for p in prod:
        print(p.id, p.products,
              p.products_date,
              p.customer_id.name)

print('Good')
