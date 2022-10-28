from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from mangum import Mangum
import os

stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"

# Este comando cria as migrações no banco de dados
models.Base.metadata.create_all(bind=engine)

app_flix_ = FastAPI(title="App-Flix", openapi_prefix=openapi_prefix)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app_flix_.get("/api/v1/videos/")
def get_all_video(db: Session = Depends(get_db)):
	return crud.get_all_video(db=db)

@app_flix_.get("/api/v1/video/{video_id}", response_model=schemas.Video)
def get_video_id(video_id: int, db: Session = Depends(get_db)):
	return crud.get_video(db=db, video_id=video_id)

@app_flix_.post("/api/v1/create_video/", response_model=schemas.VideoBase)
def create_video(video: schemas.VideoBase,
		db: Session = Depends(get_db)
	):
	return crud.create_video(db=db, video=video)

@app_flix_.put("/api/v1/video/{video_id}", response_model=schemas.VideoBase)
def update_video(video_id: int, video: schemas.VideoBase, db: Session = Depends(get_db)):
	return crud.update_video(db=db, video_id=video_id, video=video)

@app_flix_.delete("/api/v1/video/{video_id}")
def delete_video_id(video_id: int, db: Session = Depends(get_db)):
	return crud.delete_video(db=db, video_id=video_id)

handler = Mangum(app_flix_)
