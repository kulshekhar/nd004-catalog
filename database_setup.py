from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, event

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)

    # We need name to be unique because the project requires
    # the URLs to identify a category uniquely by name and
    # not by ID. This is also why this is referenced as the
    # foreign key in the Item table
    name = Column(String(250), unique=True, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)

    # We need name to be unique because the project requires
    # the URLs to identify an item uniquely by name and
    # not by ID.
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(250))
    category_name = Column(Integer, ForeignKey('category.name'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category_name,
        }


engine = create_engine('sqlite:///catalog.db')


# SQLite doesn't enforce foreign key constraints by default.
# This function configures SQLite to enforce foreign key
# constraints in connections made from this application.
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

Base.metadata.create_all(engine)
