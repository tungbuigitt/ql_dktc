from pydantic import BaseModel

class MonHocBase(BaseModel):
    ten_mon: str
    so_tin_chi: int

class MonHocCreate(MonHocBase):
    pass

class MonHocUpdate(MonHocBase):
    pass

class MonHocInDB(MonHocBase):
    id: int

    class Config:
        orm_mode = True
