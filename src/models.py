import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import func
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table user.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    profile = relationship("Profile", backref="User", uselist=False)
    posts = relationship("Post", backref="User")
    followers = relationship("FollowRequest", backref="Following", foreign_keys=["following_id"])
    followingto = relationship("FollowRequest", backref="Follower", foreign_keys=["follower_id"])


class Profile(Base):
    __tablename__ = 'Profile'
    # Here we define columns for the table profile.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    name = Column(String(250), nullable=False)
    photo = Column(String(250), nullable=False)
    biography = Column(String(250), nullable=False)

class FollowRequest(Base):
    __tablename__ = 'FollowRequest'
    # Here we define columns for the table followrequest.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('User.id'))
    following_id = Column(Integer, ForeignKey('User.id'))
    status = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table post.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    caption = Column(String(250), nullable=False)
    media_type = Column(String(250), nullable=False)
    date = Column(DateTime, default=func.now())
    location = Column(String(250), nullable=False)

class Comment(Base):
    __tablename__ = 'Comment'
    # Here we define columns for the table comment.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.id'))
    author_id = Column(Integer, ForeignKey('User.id'))
    text = Column(Integer, ForeignKey('User.id'))
    date = Column(DateTime)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e