from sqlmodel import SQLModel, Field

class Estudiante(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    modelo: str
    numero_vin: str
    año: str
    tipo: str
    nombre: str
    telefono: str