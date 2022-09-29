from collections import namedtuple

Basquetbolista = namedtuple("Basquetbolista", ["altura", "dobles", "triples","equipo"])
jordan = Basquetbolista(altura=2.0, dobles=1000, triples=5000, equipo="Chicago Bulls")
print(jordan)


import random

lista = [1,2,3]
print(random.choice(lista))
print(random.choices(lista,k=1))
print(random.randrange(0,11))
print(random.randrange(0,11, 2))


from datetime import datetime, timedelta

ahora = datetime.now()
print(ahora)

a = datetime(year=2021, month=2, day=1)
b = datetime(year=2022, month=2, day=2)

c = b - a
print(type(c))
print(c)

timedelta(weeks=52) - timedelta(weeks=10)
datetime(year=2010, month=1, day=1) + timedelta(weeks=10)

