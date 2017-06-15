from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User, engine

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

default_user = User(id=1, name="Default User", email="defaultuser@example.com")
session.add(default_user)

category1 = Category(id=1, name='Soccer')
category2 = Category(id=2, name='Basketball')
category3 = Category(id=3, name='Baseball')
category4 = Category(id=4, name='Frisbee')
category5 = Category(id=5, name='Snowboarding')
category6 = Category(id=6, name='Rock Climbing')
category7 = Category(id=7, name='Foosball')
category8 = Category(id=8, name='Skating')
category9 = Category(id=9, name='Hockey')

session.add(category1)
session.add(category2)
session.add(category3)
session.add(category4)
session.add(category5)
session.add(category6)
session.add(category7)
session.add(category8)
session.add(category9)

item1 = Item(id=1, name='Item 1',
             description='default description',
             category=category1,
             user=default_user)
item2 = Item(id=2, name='Item 2',
             description='default description',
             category=category1,
             user=default_user)
item3 = Item(id=3, name='Item 3',
             description='default description',
             category=category1,
             user=default_user)

item4 = Item(id=4, name='Item 4',
             description='default description',
             category=category2,
             user=default_user)
item5 = Item(id=5, name='Item 5',
             description='default description',
             category=category2,
             user=default_user)

item6 = Item(id=6, name='Item 6',
             description='default description',
             category=category3,
             user=default_user)

item7 = Item(id=7, name='Item 7',
             description='default description',
             category=category4,
             user=default_user)
item8 = Item(id=8, name='Item 8',
             description='default description',
             category=category4,
             user=default_user)

item9 = Item(id=9, name='Item 9',
             description='default description',
             category=category5,
             user=default_user)
item10 = Item(id=10, name='Item 10',
              description='default description',
              category=category5,
              user=default_user)

item11 = Item(id=11, name='Item 11',
              description='default description',
              category=category6,
              user=default_user)
item12 = Item(id=12, name='Item 12',
              description='default description',
              category=category6,
              user=default_user)
item13 = Item(id=13, name='Item 13',
              description='default description',
              category=category6,
              user=default_user)

item14 = Item(id=14, name='Item 14',
              description='default description',
              category=category7,
              user=default_user)
item15 = Item(id=15, name='Item 15',
              description='default description',
              category=category7,
              user=default_user)

item16 = Item(id=16, name='Item 16',
              description='default description',
              category=category8,
              user=default_user)

item17 = Item(id=17, name='Item 17',
              description='default description',
              category=category9,
              user=default_user)
item18 = Item(id=18, name='Item 18',
              description='default description',
              category=category9,
              user=default_user)
item19 = Item(id=19, name='Item 19',
              description='default description',
              category=category9,
              user=default_user)
item20 = Item(id=20, name='Item 20',
              description='default description',
              category=category9,
              user=default_user)

session.add(item1)
session.add(item2)
session.add(item3)
session.add(item4)
session.add(item5)
session.add(item6)
session.add(item7)
session.add(item8)
session.add(item9)
session.add(item10)
session.add(item11)
session.add(item12)
session.add(item13)
session.add(item14)
session.add(item15)
session.add(item16)
session.add(item17)
session.add(item18)
session.add(item19)
session.add(item20)

session.commit()

print('Added categories')
