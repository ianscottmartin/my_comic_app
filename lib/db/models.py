from sqlalchemy import Column, Integer, String
from .base import Base


class Fanboy(Base):
    __tablename__ = 'fanboys'
    id = Column(Integer, primary_key =True)
    username = Column(String, unique=True)
    
    def __repr__(self):
        return  "\n<User "\
        + f"id={self.id}, "\
        + f"username={self.username}, "\
        ">"