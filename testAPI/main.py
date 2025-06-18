from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Mahasiswa(BaseModel):
    nama: str
    nim: str
    gender: str

data_mahasiswa = [
    {"nama": "Ilham Rismawan", "nim": "12345", "gender": "Laki-laki"},
    {"nama": "Siti Aminah", "nim": "67890", "gender": "Perempuan"},
]

@app.get("/mahasiswa", response_model=List[Mahasiswa])
def get_mahasiswa():
    return data_mahasiswa

@app.post("/mahasiswa", response_model=Mahasiswa)
def add_mahasiswa(mahasiswa: Mahasiswa):
    data_mahasiswa.append(mahasiswa.dict())
    return mahasiswa
