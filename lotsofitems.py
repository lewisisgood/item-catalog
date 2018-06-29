# EDIT THIS!!!!!!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Items for Soccer
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()

item2 = Item(user_id=1, name="Shinguards", description="They protect your shins",
             category=category1)

session.add(item2)
session.commit()


item1 = Item(user_id=1, name="Soccer ball", description="To kick",
             category=category1)

session.add(item1)
session.commit()


# Items for Tennis
category2 = Category(user_id=1, name="Tennis")

session.add(category2)
session.commit()

item2 = Item(user_id=1, name="Racket", description="To hit with",
             category=category2)

session.add(item2)
session.commit()


item1 = Item(user_id=1, name="Tennis ball", description="To hit",
             category=category2)

session.add(item1)
session.commit()

# Items for Baseball
category3 = Category(user_id=1, name="Baseball")

session.add(category3)
session.commit()

# Items for Basketball
category4 = Category(user_id=1, name="Basketball")

session.add(category4)
session.commit()

# Items for Football
category5 = Category(user_id=1, name="Football")
session.add(category5)
session.commit()

# Items for Squash
category6 = Category(user_id=1, name="Squash")

session.add(category6)
session.commit()

# Items for Rugby
category7 = Category(user_id=1, name="Rugby")

session.add(category7)
session.commit()


print "added categories and items!"
