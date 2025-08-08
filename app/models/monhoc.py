from sqlalchemy import Column, Integer, String
from app.database import Base

class MonHoc(Base):
    __tablename__ = "monhoc"

    id = Column(Integer, primary_key=True, index=True)
    ten_mon = Column(String, index=True)
    so_tin_chi = Column(Integer)
