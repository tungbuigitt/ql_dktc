from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models
from app.schemas import sinhvien as schemas

router = APIRouter(prefix="/sinhvien", tags=["SinhVien"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.SinhVienOut)
def create_sinhvien(sv: schemas.SinhVienCreate, db: Session = Depends(get_db)):
    db_sv = db.query(models.SinhVien).filter(models.SinhVien.MaSV == sv.MaSV).first()
    if db_sv:
        raise HTTPException(status_code=400, detail="Mã sinh viên đã tồn tại")
    new_sv = models.SinhVien(**sv.dict())
    db.add(new_sv)
    db.commit()
    db.refresh(new_sv)
    return new_sv

@router.get("/", response_model=list[schemas.SinhVienOut])
def list_sinhvien(db: Session = Depends(get_db)):
    return db.query(models.SinhVien).all()

@router.get("/{masv}", response_model=schemas.SinhVienOut)
def get_sinhvien(masv: str, db: Session = Depends(get_db)):
    sv = db.query(models.SinhVien).filter(models.SinhVien.MaSV == masv).first()
    if not sv:
        raise HTTPException(status_code=404, detail="Không tìm thấy sinh viên")
    return sv

@router.put("/{masv}", response_model=schemas.SinhVienOut)
def update_sinhvien(masv: str, sv_data: schemas.SinhVienUpdate, db: Session = Depends(get_db)):
    sv = db.query(models.SinhVien).filter(models.SinhVien.MaSV == masv).first()
    if not sv:
        raise HTTPException(status_code=404, detail="Không tìm thấy sinh viên")
    for key, value in sv_data.dict().items():
        setattr(sv, key, value)
    db.commit()
    db.refresh(sv)
    return sv

@router.delete("/{masv}")
def delete_sinhvien(masv: str, db: Session = Depends(get_db)):
    sv = db.query(models.SinhVien).filter(models.SinhVien.MaSV == masv).first()
    if not sv:
        raise HTTPException(status_code=404, detail="Không tìm thấy sinh viên")
    db.delete(sv)
    db.commit()
    return {"message": "Đã xóa sinh viên"}
