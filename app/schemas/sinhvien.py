from pydantic import BaseModel

class SinhVienBase(BaseModel):
    HoTen: str
    NgaySinh: str
    GioiTinh: str
    Khoa: str
    SDT: str

class SinhVienCreate(SinhVienBase):
    MaSV: str

class SinhVienUpdate(SinhVienBase):
    pass

class SinhVienOut(SinhVienBase):
    MaSV: str

    class Config:
        orm_mode = True
