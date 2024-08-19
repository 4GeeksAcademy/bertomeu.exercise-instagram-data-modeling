import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    userId = Column(Integer, primary_key=True)
    userName = Column(String(25), unique=True, nullable=False)
    firstName = Column(String(25))
    lastName = Column(String(25))
    email = Column(String(50), unique=True, nullable=False)
    

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    addressId = Column(Integer, primary_key=True)
    streetName = Column(String(50))
    streetNumber = Column(String(10))
    postcode = Column(String(10), nullable=False)
    personId = Column(Integer, ForeignKey('user.userId'))
    person = relationship(User)

    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    postId = Column(Integer, primary_key=True)
    postText = Column(String(200), nullable=False)
    authorId = Column(Integer, ForeignKey('user.userId'))
    author = relationship(User) 

    def to_dict(self):
        return {}      

  

class Comment(Base):
    __tablename__ = 'comment'
    commentId = Column(Integer, primary_key=True)
    commentText = Column(String(200), nullable=False)
    authorId = Column(Integer, ForeignKey('user.userId'))
    authorRelationship = relationship(User)
    postId = Column(Integer, ForeignKey('post.postId'))
    post = relationship(Post)

    def to_dict(self):
        return {}

class Follower(Base):
    __tablename__ = 'follower'
    followerId = Column(Integer, primary_key=True)
    userFromId = Column(Integer, ForeignKey('user.userId'))
    userFrom = relationship(User)
    userToId = Column(Integer, ForeignKey('user.userId'))
    userTo = relationship(User)    



    def to_dict(self):
        return {}
   

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
