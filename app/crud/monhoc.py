from sqlalchemy.orm import Session
from app.models import monhoc as models
from app.schemas import monhoc as schemas

#lay tat ca cac mon
def get_all(db: Session):
    return db.query(models.MonHoc).all()

#lay mon theo ma mon
def get_by_id(db: Session, id: int):
    return db.query(models.MonHoc).filter(models.MonHoc.id == id).first()

#tao them mon hoc
def create(db: Session, monhoc: schemas.MonHocCreate):
    db_mon = models.MonHoc(**monhoc.dict())
    db.add(db_mon)
    db.commit()
    db.refresh(db_mon)
    return db_mon

#cap nhat thong tin mon hoc
def update(db: Session, id: int, monhoc: schemas.MonHocUpdate):
    db_mon = get_by_id(db, id)
    if db_mon:
        for attr, value in monhoc.dict().items():
            setattr(db_mon, attr, value)
        db.commit()
        db.refresh(db_mon)
    return db_mon

#xoa mon hoc
def delete(db: Session, id: int):
    db_mon = get_by_id(db, id)
    if db_mon:
        db.delete(db_mon)
        db.commit()
    return db_mon
