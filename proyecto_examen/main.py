from fastapi import (FastAPI, HTTPException, status,
                    Request, Query)
from database import engine, inicializar_bd
from sqlmodel import Session, select
from models import vehiculo
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

inicializar_bd()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Monta la carpeta frontend en la raíz
app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

@app.get("/")
def read_root():
    return {"Hello": "Hello World"}

# CRUD
# CREATE
# READ
# UPDATE Actualizar
# DELETE

@app.get("/vehiculos")
def leer_estudiantes(resquest:Request, 
                     skip:int = Query(0, ge=0),
                     limit:int = Query(10, ge=1)
                     ):                                          
    with Session(engine) as session:
        total = session.exec(select(Vehiculos)).all()
        total_conteo = len(total)
        estudiantes_pagina = session.exec(
            select(Vehiculo).offset(skip).limit(limit)
        ).all()
        base_url = str(resquest.url).split('?')[0]
        siguiente_skip = skip + limit
        anterior_skip = max(0, skip-limit)
        siguiente_url = f"{base_url}?skip={siguiente_skip}&limit={limit}" if siguiente_skip < total_conteo else None
        anterior_url = f"{base_url}?skip={anterior_skip}&limit={limit}" if skip > 0 else None
        return {
            "count": total_conteo,
            "next": siguiente_url,
            "previous": anterior_url,
            "details": vehiculo_pagina
        }

@app.get("/vehiculos/{matricula}", response_model=Vehiculo)
def leer_vehiculo(matricula:str):
    with Session(engine) as session:
        evehiculos = session.get(vehiculo, matricula)
        if not vehiculose:
            raise HTTPException(status_code=404, detail="El estudiante no encontrado")
        return vehiculos
    
@app.post("/vehiculos", response_model=Vehiculo, 
          status_code=status.HTTP_201_CREATED)
def crear_vehiculo(vehiculo:Vehiculo):
    with Session(engine) as session:
        session.add(vehiculo)
        session.commit()
        session.refresh(vehiculo)
        return evehiculo
    
@app.delete("/vehiculos/{modelo}", 
            status_code=status.HTTP_204_NO_CONTENT)
def eliminar_vehiculo(modelo:str):
    with Session(engine) as session:
        vehiculos = session.get(Vehiculo, modelo)
        if not vehiculos:
            raise HTTPException(status_code=404, 
                                detail="El vehículo no encontrado")
        session.delete(vehiculo)
        session.commit()

@app.put("/vehiculos/{modelo}", response_model=Vehiculo)
def actualizar_vehiculos+(modelo:str, 
                          vehiculo_actualizar:Vehiculo):
    with Session(engine) as session:
        vehiculos = session.get(Vehiculos, modelo)
        if not vehiculo:
            raise HTTPException(status_code=404, 
                                detail="El vehículo no encontrado")
        vehiculo.vim = vehiculo_actualizar.vim
        vehiculo.anio = vehiculo_actualizar.año
        vehiculo.tipo = vehiculo_actualizar.tipo
        vehiculo.propietario = vehiculo_actualizar.propietario
        vehiculoe.telefono = vehiculo_actualizar.telefono

        session.add(vehiculo)
        session.commit()
        session.refresh(vehiculo)
        return vehiculo33333

@app.get("/vehiculos")
def leer_vehiculos(request: Request, 
                   skip: int = Query(0, ge=0),
                   limit: int = Query(10, ge=1)):
    with Session(engine) as session:
        total = session.exec(select(Vehiculo)).all()
        total_conteo = len(total)
        vehiculos_pagina = session.exec(
            select(Vehiculo).offset(skip).limit(limit)
        ).all()
        base_url = str(request.url).split('?')[0]
        siguiente_skip = skip + limit
        anterior_skip = max(0, skip-limit)
        siguiente_url = f"{base_url}?skip={siguiente_skip}&limit={limit}" if siguiente_skip < total_conteo else None
        anterior_url = f"{base_url}?skip={anterior_skip}&limit={limit}" if skip > 0 else None
        return {
            "count": total_conteo,
            "next": siguiente_url,
            "previous": anterior_url,
            "details": vehiculos_pagina
        }

@app.get("/vehiculos/{modelo}", response_model=Vehiculo)
def leer_vehiculo(modelo: str):
    with Session(engine) as session:
        vehiculo = session.get(Vehiculo, modelo)
        if not vehiculo:
            raise HTTPException(status_code=404, detail="El vehículo no encontrado")
        return vehiculo

@app.post("/vehiculos", response_model=Vehiculo, status_code=status.HTTP_201_CREATED)
def crear_vehiculo(vehiculo: Vehiculo):
    with Session(engine) as session:
        session.add(vehiculo)
        session.commit()
        session.refresh(vehiculo)
        return vehiculo

@app.delete("/vehiculos/{modelo}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_vehiculo(modelo: str):
    with Session(engine) as session:
        vehiculo = session.get(Vehiculo, modelo)
        if not vehiculo:
            raise HTTPException(status_code=404, detail="El vehículo no encontrado")
        session.delete(vehiculo)
        session.commit()

@app.put("/vehiculos/{modelo}", response_model=Vehiculo)
def actualizar_vehiculo(modelo: str, vehiculo_actualizar: Vehiculo):
    with Session(engine) as session:
        vehiculo = session.get(Vehiculo, modelo)
        if not vehiculo:
            raise HTTPException(status_code=404, detail="El vehículo no encontrado")
        vehiculo.vim = vehiculo_actualizar.vim
        vehiculo.anio = vehiculo_actualizar.anio
        vehiculo.tipo = vehiculo_actualizar.tipo
        vehiculo.propietario = vehiculo_actualizar.propietario
        vehiculo.telefono = vehiculo_actualizar.telefono

        session.add(vehiculo)
        session.commit()
        session.refresh(vehiculo)
        return vehiculo