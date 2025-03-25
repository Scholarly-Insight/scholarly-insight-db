from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# User Pydantic Schema
class UserCreate(BaseModel):
    name: str
    email: str
    password_hash: str

class User(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Author Pydantic Schema
class AuthorCreate(BaseModel):
    first_name: str
    last_name: str

class Author(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        orm_mode = True

# Article Pydantic Schema
class ArticleCreate(BaseModel):
    title: str
    abstract: str
    published_date: datetime
    category: str
    journal: str
    doi: str
    link: str
    authors: List[int]

class Article(BaseModel):
    id: int
    title: str
    abstract: str
    published_date: datetime
    category: str
    journal: str
    doi: str
    link: str
    created_at: datetime
    authors: List[Author]

    class Config:
        orm_mode = True

# Article-Author Pydantic Schema
class ArticleAuthorCreate(BaseModel):
    article_id: int
    author_id: int

class ArticleAuthor(BaseModel):
    article_id: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# UserAlert Pydantic Schema
class UserAlertCreate(BaseModel):
    user_id: int
    category: str
    alert_type: str

class UserAlert(BaseModel):
    id: int
    user_id: int
    category: str
    description: Optional[str] = None
    alert_type: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# UserCollection Pydantic Schema
class UserCollectionCreate(BaseModel):
    user_id: int
    article_id: int

class UserCollection(BaseModel):
    collection_id: int
    user_id: int
    article_id: int
    saved_date: datetime

    class Config:
        orm_mode = True

# UserHistory Pydantic Schema
class UserHistoryCreate(BaseModel):
    user_id: int
    article_id: int

class UserHistory(BaseModel):
    id: int
    user_id: int
    article_id: int
    viewed_date: datetime

    class Config:
        orm_mode = True
