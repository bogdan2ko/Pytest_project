from sqlalchemy import  Column, Integer, String, DateTime

from db import Model
from sqlalchemy import func # Assuming func is imported from sqlalchemy




class Films(Model):
    __tablename__ = 'actor'

    actor_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_update = Column(DateTime(), nullable=False, default=func.now(), onupdate=func.now())
