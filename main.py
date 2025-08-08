from fastapi import FastAPI
from app.database import engine, Base
from app.routers import giangvien, monhoc, kyhoc, sinhvien, khoa, dangky

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(monhoc.router, prefix="/monhoc", tags=["MonHoc"])
app.include_router(kyhoc.router, prefix="/kyhoc", tags=["KyHoc"])
app.include_router(giangvien.router, prefix="/giangvien", tags=["GiangVien"])
app.include_router(sinhvien.router, prefix="/sinhvien", tags=["SinhVien"])
app.include_router(khoa.router, prefix="/khoa", tags=["Khoa"])
app.include_router(dangky.router, prefix="/dangky", tags=["DangKyTinChi"])
