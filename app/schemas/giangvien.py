from pydantic import BaseModel

class GiangVienBase(BaseModel):
    HoTen : str
    Khoa : str
    Email : str
    SDT : str

class GiangVienCreate(GiangVienBase):
    MaGV : str    

class GiangVienUpdate(GiangVienBase):
    pass

class GiangVienOut(GiangVienBase):
    MaGV : str

    class Config:
        orm_mode = True

