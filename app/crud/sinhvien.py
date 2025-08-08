from sqlalchemy.orm import Session
from app.models.sinhvien import SinhVien
from app.schemas.sinhvien import SinhVienCreate, SinhVienUpdate

def get_sinhvien(db: Session, ma_sv: str):
    return db.query(SinhVien).filter(SinhVien.MaSV == ma_sv).first()

def get_all_sinhvien(db: Session):
    return db.query(SinhVien).all()

def create_sinhvien(db: Session, sv: SinhVienCreate):
    db_sv = SinhVien(**sv.dict())
    db.add(db_sv)
    db.commit()
    db.refresh(db_sv)
    return db_sv

def update_sinhvien(db: Session, ma_sv: str, data: SinhVienUpdate):
    db_sv = get_sinhvien(db, ma_sv)
    if db_sv:
        for key, value in data.dict().items():
            setattr(db_sv, key, value)
        db.commit()
        db.refresh(db_sv)
    return db_sv

def delete_sinhvien(db: Session, ma_sv: str):
    db_sv = get_sinhvien(db, ma_sv)
    if db_sv:
        db.delete(db_sv)
        db.commit()
    return db_sv
