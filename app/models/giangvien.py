from sqlalchemy import Column, String
from app.database import Base

class Giangvien(Base):
    __tablename__="giangvien"

    MaGV = Column(String(10),primary_key=True, index=True) 
    HoTen = Column(String(20), nullable=False)
    Khoa = Column(String(10))
    Email = Column(String(50),unique=True, nullable=False, index=True)
    SDT = Column(String(15))
