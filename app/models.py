from database import Base
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime

# User Table
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    password_hash = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

# Author Table
class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))

    # Relationship with Article via article_author
    articles = relationship('Article', secondary='article_author', back_populates='authors')

# Article Table
class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))
    abstract = Column(Text)
    published_date = Column(Date)
    category = Column(String(100))
    journal = Column(String(255))
    doi = Column(String(255))
    link = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    # Relationship with Author via article_author
    authors = relationship('Author', secondary='article_author', back_populates='articles')

# Article-Author Table (many-to-many relationship)
class ArticleAuthor(Base):
    __tablename__ = 'article_author'

    article_id = Column(Integer, ForeignKey('article.id'), primary_key=True)
    author_id = Column(Integer, ForeignKey('author.id'), primary_key=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

# User Alert Table
class UserAlert(Base):
    __tablename__ = 'user_alert'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    category = Column(String(100))
    description = Column(Text)
    alert_type = Column(String(50))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

# User Collection Table
class UserCollection(Base):
    __tablename__ = 'user_collection'

    collection_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    article_id = Column(Integer, ForeignKey('article.id'))
    saved_date = Column(TIMESTAMP, default=datetime.utcnow)

# User History Table
class UserHistory(Base):
    __tablename__ = 'user_history'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    article_id = Column(Integer, ForeignKey('article.id'))
    viewed_date = Column(TIMESTAMP, default=datetime.utcnow)
