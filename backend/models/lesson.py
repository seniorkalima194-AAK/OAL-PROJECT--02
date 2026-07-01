from sqlalchemy import Column, Integer,String, Text
from database import Base

class Lesson(Base):
    __tablename__="lessons"

    id=Column(Integer,primary_key=True, index=True)
    subject=Column(String,index=True)
    title=Column(String,index=True)
    content=Column(Text)
    estimated_time=Column(Integer)
