from sqlalchemy.orm import Session
from app.models.giangvien import Giangvien
from app.schemas.giangvien import GiangVienCreate,GiangVienUpdate

def get_giangvien(db: Session, ma_gv: str):
    return db.query(Giangvien).filter(Giangvien.MaGV == ma_gv).first()

def get_all_giangvien(db: Session):
    return db.query(Giangvien).all()

def create_giangvien(db: Session, sv: GiangVienCreate):
    db_sv = Giangvien(**sv.dict())
    db.add(db_sv)
    db.commit()
    db.refresh(db_sv)
    return db_sv

def update_giangvien(db: Session, ma_sv: str, data: GiangVienUpdate):
    db_sv = get_giangvien(db, ma_sv)
    if db_sv:
        for key, value in data.dict().items():
            setattr(db_sv, key, value)
        db.commit()
        db.refresh(db_sv)
    return db_sv

def delete_giangvien(db: Session, ma_sv: str):
    db_sv = get_giangvien(db, ma_sv)
    if db_sv:
        db.delete(db_sv)
        db.commit()
    return db_sv

