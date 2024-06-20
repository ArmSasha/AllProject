from sqlalchemy import Column, BigInteger, String, Float, sql

from utils.db_api.db_gino import BaseModel


class Groups(BaseModel):
    __tablename__ = 'groups'
    chat_id = Column(BigInteger)
    group_id = Column(BigInteger, primary_key=True)
    group_name = Column(String)
    group_link = Column(String, primary_key=True)

    query: sql.select
