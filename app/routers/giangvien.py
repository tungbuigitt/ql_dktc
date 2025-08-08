from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models
from app.schemas import giangvien as schemas

router = APIRouter(prefix="/giangvien", tags=["GiangVien"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.GiangVienOut)
def create_giangvien(gv: schemas.GiangVienCreate, db: Session = Depends(get_db)):
    db_gv = db.query(models.GiangVien).filter(models.GiangVien.MaGV == gv.MaGV).first()
    if db_gv:
        raise HTTPException(status_code=400, detail="Mã giảng viên đã tồn tại")
    new_gv = models.GiangVien(**gv.dict())
    db.add(new_gv)
    db.commit()
    db.refresh(new_gv)
    return new_gv

@router.get("/", response_model=list[schemas.GiangVienOut])
def list_giangvien(db: Session = Depends(get_db)):
    return db.query(models.GiangVien).all()

@router.get("/{magv}", response_model=schemas.GiangVienOut)
def get_giangvien(magv: str, db: Session = Depends(get_db)):
    gv = db.query(models.GiangVien).filter(models.GiangVien.MaGV == magv).first()
    if not gv:
        raise HTTPException(status_code=404, detail="Không tìm thấy giảng viên")
    return gv

@router.put("/{magv}", response_model=schemas.GiangVienOut)
def update_giangvien(magv: str, gv_data: schemas.GiangVienUpdate, db: Session = Depends(get_db)):
    gv = db.query(models.GiangVien).filter(models.GiangVien.MaGV == magv).first()
    if not gv:
        raise HTTPException(status_code=404, detail="Không tìm thấy giảng viên")
    for key, value in gv_data.dict().items():
        setattr(gv, key, value)
    db.commit()
    db.refresh(gv)
    return gv

@router.delete("/{magv}")
def delete_giangvien(magv: str, db: Session = Depends(get_db)):
    gv = db.query(models.GiangVien).filter(models.GiangVien.MaGV == magv).first()
    if not gv:
        raise HTTPException(status_code=404, detail="Không tìm thấy giảng viên")
    db.delete(gv)
    db.commit()
    return {"message": "Đã xóa giảng viên"}