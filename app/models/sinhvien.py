from sqlalchemy import Column, String
from app.database import Base

class SinhVien(Base):
    __tablename__ = "sinhvien"

    MaSV = Column(String(10), primary_key=True, index=True)
    HoTen = Column(String(100), nullable=False)
    NgaySinh = Column(Date(20))
    GioiTinh = Column(String(10))
    Khoa = Column(String(10))
    SDT = Column(String(15))
