from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import monhoc as schemas
from app.crud import monhoc as crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.MonHocInDB)
def create(monhoc: schemas.MonHocCreate, db: Session = Depends(get_db)):
    return crud.create(db, monhoc)

@router.get("/", response_model=list[schemas.MonHocInDB])
def read_all(db: Session = Depends(get_db)):
    return crud.get_all(db)

@router.get("/{id}", response_model=schemas.MonHocInDB)
def read_one(id: int, db: Session = Depends(get_db)):
    db_mon = crud.get_by_id(db, id)
    if not db_mon:
        raise HTTPException(status_code=404, detail="Môn học không tồn tại")
    return db_mon

@router.put("/{id}", response_model=schemas.MonHocInDB)
def update(id: int, monhoc: schemas.MonHocUpdate, db: Session = Depends(get_db)):
    return crud.update(db, id, monhoc)

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    crud.delete(db, id)
    return {"ok": True}
